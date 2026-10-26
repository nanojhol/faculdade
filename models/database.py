"""
Camada Model (Padrão MVC)
Responsável pelo acesso, integridade e manipulação dos dados no banco SQLite (3FN).
"""

import os
import sqlite3
from typing import Any, Dict, List, Optional

DB_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'database.db')
SCHEMA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'schema.sql')

# Mapeamento oficial dos 5 sabores para seus respectivos arquivos de imagem
MAPA_IMAGENS = {
    'Chocolate': 'img/chocolate.jpg',
    'Ninho com Brigadeiro': 'img/ninho-brigadeiro.jpg',
    'Ninho com Morango': 'img/ninho-morango.jpg',
    'Nutella': 'img/nutella.jpg',
    'Doce de Leite': 'img/doce-de-leite.jpg'
}


def get_db_connection() -> sqlite3.Connection:
    """Retorna uma conexão ativa com o SQLite com integridade referencial e dicionário de linhas."""
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Inicializa as tabelas e dados iniciais conforme o schema.sql se o banco não existir."""
    if not os.path.exists(DB_FILE) or os.path.getsize(DB_FILE) == 0:
        conn = get_db_connection()
        with open(SCHEMA_FILE, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()


# =====================================================================
# OPERAÇÕES DE PRODUTOS (CATÁLOGO DE CUPCAKES)
# =====================================================================

def listar_produtos() -> List[Dict[str, Any]]:
    """Retorna todos os cupcakes disponíveis no catálogo com suas respectivas imagens."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos WHERE disponivel = 1 ORDER BY id ASC;")
    rows = cursor.fetchall()
    conn.close()
    produtos = []
    for row in rows:
        p = dict(row)
        p['imagem'] = MAPA_IMAGENS.get(p['nome'], 'img/chocolate.jpg')
        produtos.append(p)
    return produtos


def buscar_produto_por_id(produto_id: int) -> Optional[Dict[str, Any]]:
    """Busca um cupcake específico pelo seu ID e anexa a imagem correspondente."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?;", (produto_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    p = dict(row)
    p['imagem'] = MAPA_IMAGENS.get(p['nome'], 'img/chocolate.jpg')
    return p


# =====================================================================
# OPERAÇÕES DE CLIENTES (CADASTRO E AUTENTICAÇÃO)
# =====================================================================

def criar_cliente(nome: str, email: str, senha_hash: str, telefone: str = "", endereco: str = "") -> int:
    """Cadastra um novo cliente no sistema e retorna o ID gerado."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO clientes (nome, email, senha_hash, telefone, endereco_padrao)
        VALUES (?, ?, ?, ?, ?);
        """,
        (nome, email, senha_hash, telefone, endereco)
    )
    conn.commit()
    cliente_id = cursor.lastrowid
    conn.close()
    return cliente_id


def buscar_cliente_por_email(email: str) -> Optional[Dict[str, Any]]:
    """Localiza um cliente pelo e-mail informado."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE email = ?;", (email.strip().lower(),))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def buscar_cliente_por_id(cliente_id: int) -> Optional[Dict[str, Any]]:
    """Localiza um cliente pelo seu ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, telefone, endereco_padrao FROM clientes WHERE id = ?;", (cliente_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def atualizar_endereco_cliente(cliente_id: int, novo_endereco: str) -> bool:
    """Atualiza o endereço cadastral/padrão do cliente."""
    if not novo_endereco or not novo_endereco.strip():
        return False
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE clientes SET endereco_padrao = ? WHERE id = ?;",
        (novo_endereco.strip(), cliente_id)
    )
    conn.commit()
    alterado = cursor.rowcount > 0
    conn.close()
    return alterado


# =====================================================================
# OPERAÇÕES DE PEDIDOS E ITENS (CHECKOUT E ACOMPANHAMENTO)
# =====================================================================

def criar_pedido(
    cliente_id: int,
    valor_produtos: float,
    taxa_entrega: float,
    forma_pagamento: str,
    endereco_entrega: str,
    itens: List[Dict[str, Any]],
    observacoes: str = ""
) -> int:
    """
    Cria uma nova ordem de pedido e seus itens associados (relação N:M resolvida em 3FN).
    Garante atomicidade através de transação com commit.
    """
    valor_total = round(valor_produtos + taxa_entrega, 2)
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO pedidos (
                cliente_id, valor_produtos, taxa_entrega, valor_total,
                forma_pagamento, status_pagamento, status_entrega,
                endereco_entrega, prazo_estimado, observacoes
            ) VALUES (?, ?, ?, ?, ?, 'CONFIRMADO', 'RECEBIDO', ?, '15 a 30 minutos', ?);
            """,
            (cliente_id, valor_produtos, taxa_entrega, valor_total, forma_pagamento, endereco_entrega, observacoes)
        )
        pedido_id = cursor.lastrowid

        for item in itens:
            cursor.execute(
                """
                INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario, subtotal)
                VALUES (?, ?, ?, ?, ?);
                """,
                (
                    pedido_id,
                    item['produto_id'],
                    item['quantidade'],
                    item['preco_unitario'],
                    round(item['quantidade'] * item['preco_unitario'], 2)
                )
            )

        conn.commit()
        return pedido_id
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def buscar_pedido_por_id(pedido_id: int) -> Optional[Dict[str, Any]]:
    """Retorna os dados completos do pedido e seus itens."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT p.*, c.nome as cliente_nome, c.telefone as cliente_telefone
        FROM pedidos p
        JOIN clientes c ON p.cliente_id = c.id
        WHERE p.id = ?;
        """,
        (pedido_id,)
    )
    pedido_row = cursor.fetchone()

    if not pedido_row:
        conn.close()
        return None

    pedido = dict(pedido_row)

    cursor.execute(
        """
        SELECT ip.*, prod.nome as produto_nome, prod.categoria as produto_categoria
        FROM itens_pedido ip
        JOIN produtos prod ON ip.produto_id = prod.id
        WHERE ip.pedido_id = ?;
        """,
        (pedido_id,)
    )
    itens_rows = cursor.fetchall()
    pedido['itens'] = [dict(r) for r in itens_rows]

    conn.close()
    return pedido


def listar_pedidos_cliente(cliente_id: int) -> List[Dict[str, Any]]:
    """Lista o histórico de pedidos de um cliente específico."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM pedidos
        WHERE cliente_id = ?
        ORDER BY id DESC;
        """,
        (cliente_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def listar_todos_pedidos() -> List[Dict[str, Any]]:
    """Lista todos os pedidos para o painel operacional da loja (HU15 / UC06)."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT p.*, c.nome as cliente_nome, c.telefone as cliente_telefone
        FROM pedidos p
        JOIN clientes c ON p.cliente_id = c.id
        ORDER BY p.id DESC;
        """
    )
    rows = cursor.fetchall()
    pedidos = [dict(r) for r in rows]

    for p in pedidos:
        cursor.execute(
            """
            SELECT ip.quantidade, prod.nome as produto_nome
            FROM itens_pedido ip
            JOIN produtos prod ON ip.produto_id = prod.id
            WHERE ip.pedido_id = ?;
            """,
            (p['id'],)
        )
        p['resumo_itens'] = ", ".join([f"{r['quantidade']}x {r['produto_nome']}" for r in cursor.fetchall()])

    conn.close()
    return pedidos


def atualizar_status_entrega(pedido_id: int, novo_status: str) -> bool:
    """Atualiza o status de entrega do pedido no painel do operador."""
    status_validos = ['RECEBIDO', 'PREPARANDO', 'EM_ROTA', 'ENTREGUE']
    if novo_status not in status_validos:
        return False

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE pedidos
        SET status_entrega = ?
        WHERE id = ?;
        """,
        (novo_status, pedido_id)
    )
    conn.commit()
    alterado = cursor.rowcount > 0
    conn.close()
    return alterado
