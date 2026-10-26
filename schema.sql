-- =====================================================================
-- PROJETO INTEGRADOR TRANSDISCIPLINAR EM ENGENHARIA DE SOFTWARE II
-- Loja de Cupcakes Gourmet — Script Físico de Banco de Dados (SQLite)
-- Padrão: 3FN (Terceira Forma Normal)
-- =====================================================================

PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------------
-- 1. TABELA: clientes
-- Armazena os dados cadastrais dos clientes da loja.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
    endereco_padrao VARCHAR(255),
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------
-- 2. TABELA: produtos
-- Armazena o catálogo oficial de cupcakes disponíveis.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(80) NOT NULL,
    descricao TEXT NOT NULL,
    preco DECIMAL(10, 2) NOT NULL CHECK (preco > 0),
    disponivel BOOLEAN NOT NULL DEFAULT 1,
    categoria VARCHAR(40) DEFAULT 'Cupcake Gourmet',
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------
-- 3. TABELA: pedidos
-- Registra as compras efetuadas, vinculadas ao cliente e endereço.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
    valor_produtos DECIMAL(10, 2) NOT NULL CHECK (valor_produtos >= 0),
    taxa_entrega DECIMAL(10, 2) NOT NULL DEFAULT 6.00 CHECK (taxa_entrega >= 0),
    valor_total DECIMAL(10, 2) NOT NULL CHECK (valor_total > 0),
    forma_pagamento VARCHAR(20) NOT NULL CHECK (forma_pagamento IN ('PIX', 'CARTAO_CREDITO')),
    status_pagamento VARCHAR(20) NOT NULL DEFAULT 'PENDENTE' CHECK (status_pagamento IN ('PENDENTE', 'CONFIRMADO', 'RECUSADO')),
    status_entrega VARCHAR(20) NOT NULL DEFAULT 'RECEBIDO' CHECK (status_entrega IN ('RECEBIDO', 'PREPARANDO', 'EM_ROTA', 'ENTREGUE')),
    endereco_entrega VARCHAR(255) NOT NULL,
    prazo_estimado VARCHAR(30) DEFAULT '15 a 30 minutos',
    observacoes TEXT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT
);

-- ---------------------------------------------------------------------
-- 4. TABELA: itens_pedido
-- Registra os produtos associados a cada pedido (relação N:M resolvida).
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS itens_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    preco_unitario DECIMAL(10, 2) NOT NULL CHECK (preco_unitario > 0),
    subtotal DECIMAL(10, 2) NOT NULL CHECK (subtotal > 0),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE,
    FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE RESTRICT
);

-- ---------------------------------------------------------------------
-- ÍNDICES PARA OTIMIZAÇÃO DE BUSCA E INTEGRIDADE
-- ---------------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_clientes_email ON clientes(email);
CREATE INDEX IF NOT EXISTS idx_pedidos_cliente ON pedidos(cliente_id);
CREATE INDEX IF NOT EXISTS idx_itens_pedido_pedido ON itens_pedido(pedido_id);
CREATE INDEX IF NOT EXISTS idx_itens_pedido_produto ON itens_pedido(produto_id);

-- =====================================================================
-- CARGA INICIAL DE DADOS (SEEDS)
-- =====================================================================

-- Carga dos 5 sabores oficiais de cupcakes definidos para a loja
INSERT INTO produtos (nome, descricao, preco, disponivel) VALUES
('Chocolate', 'Massa fofinha de cacau 100%, recheio cremoso de ganache de chocolate meio amargo e cobertura de brigadeiro gourmet tradicional.', 13.00, 1),
('Ninho com Brigadeiro', 'Massa amanteigada de baunilha, recheio generoso de leite Ninho cremoso e cobertura dupla de brigadeiro tradicional e Ninho.', 14.00, 1),
('Ninho com Morango', 'Massa leve de baunilha, recheio de geleia artesanal de morango fresco e cobertura aveludada de mousse de leite Ninho.', 15.00, 1),
('Nutella', 'Massa de cacau nobre, recheio puro de creme de avelã Nutella e cobertura de brigadeiro de Nutella com avelãs picadas.', 16.00, 1),
('Doce de Leite', 'Massa de especiarias suaves com canela, recheio e cobertura generosa de doce de leite caseiro cremoso polvilhado com canela.', 13.50, 1);

-- Cliente demonstrativo inicial para testes de pedidos e autenticação
INSERT INTO clientes (nome, email, senha_hash, telefone, endereco_padrao) VALUES
('Cliente Demonstração', 'cliente@exemplo.com', 'scrypt:32768:8:1$demo123', '(11) 98765-4321', 'Rua das Flores, 123, Bairro Doce, Cidade - SP');
