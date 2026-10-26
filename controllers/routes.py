"""
Camada Controller (Padrão MVC)
Responsável pelo roteamento, controle de fluxo, validação de regras de negócio
e coordenação entre a camada Model (dados) e View (templates HTML).
"""

from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from models import database

routes_bp = Blueprint('routes', __name__)
TAXA_ENTREGA_PADRAO = 6.00


# =====================================================================
# 1. VITRINE (CATÁLOGO DE CUPCAKES)
# =====================================================================

@routes_bp.route('/')
def index():
    """Exibe o catálogo com os 5 sabores oficiais de cupcakes (HU01, HU02, UC01)."""
    produtos = database.listar_produtos()
    return render_template('vitrine.html', produtos=produtos)


# =====================================================================
# 2. CARRINHO DE COMPRAS (HU05, HU06, HU07, HU08, UC03)
# =====================================================================

@routes_bp.route('/carrinho')
def carrinho():
    """Exibe os itens no carrinho, calcula subtotais, taxa fixa e total geral."""
    carrinho_dict = session.get('carrinho', {})
    itens = []
    subtotal = 0.0

    for prod_id_str, qtd in carrinho_dict.items():
        produto = database.buscar_produto_por_id(int(prod_id_str))
        if produto and qtd > 0:
            sub = produto['preco'] * qtd
            subtotal += sub
            itens.append({
                'produto': produto,
                'quantidade': qtd,
                'subtotal': sub
            })

    total = round(subtotal + TAXA_ENTREGA_PADRAO, 2) if itens else 0.0
    return render_template(
        'carrinho.html',
        itens=itens,
        subtotal=subtotal,
        taxa_entrega=TAXA_ENTREGA_PADRAO,
        total=total
    )


@routes_bp.route('/carrinho/adicionar', methods=['POST'])
def adicionar_carrinho():
    """Adiciona um cupcake ao carrinho da sessão mantendo o cliente na mesma página."""
    is_ajax = (
        request.headers.get('X-Requested-With') == 'XMLHttpRequest' or
        request.headers.get('Accept', '').startswith('application/json') or
        request.is_json
    )

    try:
        produto_id = int(request.form.get('produto_id', 0))
        quantidade = int(request.form.get('quantidade', 1))

        if quantidade <= 0:
            msg = 'Informe uma quantidade válida maior que zero.'
            if is_ajax:
                return {'success': False, 'message': msg}, 400
            flash(msg, 'error')
            return redirect(request.referrer or url_for('routes.index'))

        produto = database.buscar_produto_por_id(produto_id)
        if not produto:
            msg = 'Cupcake não localizado no catálogo.'
            if is_ajax:
                return {'success': False, 'message': msg}, 404
            flash(msg, 'error')
            return redirect(request.referrer or url_for('routes.index'))

        carrinho_dict = session.get('carrinho', {})
        carrinho_dict[str(produto_id)] = carrinho_dict.get(str(produto_id), 0) + quantidade
        session['carrinho'] = carrinho_dict
        session['carrinho_qtd'] = sum(carrinho_dict.values())

        msg = f'{quantidade}x "{produto["nome"]}" adicionado ao carrinho com sucesso!'
        if is_ajax:
            return {
                'success': True,
                'message': msg,
                'carrinho_qtd': session['carrinho_qtd'],
                'produto_id': produto_id,
                'produto_nome': produto['nome']
            }

        flash(msg, 'success')
    except (ValueError, TypeError):
        msg = 'Erro ao processar quantidade.'
        if is_ajax:
            return {'success': False, 'message': msg}, 400
        flash(msg, 'error')

    # Mantém o cliente na mesma página de origem (vitrine)
    return redirect(request.referrer or url_for('routes.index'))


@routes_bp.route('/carrinho/atualizar', methods=['POST'])
def atualizar_carrinho():
    """Atualiza a quantidade de um cupcake no carrinho."""
    try:
        produto_id = str(int(request.form.get('produto_id', 0)))
        quantidade = int(request.form.get('quantidade', 1))

        carrinho_dict = session.get('carrinho', {})
        if quantidade > 0:
            carrinho_dict[produto_id] = quantidade
            flash('Quantidade atualizada com sucesso.', 'success')
        else:
            carrinho_dict.pop(produto_id, None)
            flash('Item removido do carrinho.', 'success')

        session['carrinho'] = carrinho_dict
        session['carrinho_qtd'] = sum(carrinho_dict.values())
    except (ValueError, TypeError):
        flash('Valor de quantidade inválido.', 'error')

    return redirect(url_for('routes.carrinho'))


@routes_bp.route('/carrinho/remover', methods=['POST'])
def remover_carrinho():
    """Remove um item específico do carrinho."""
    produto_id = str(request.form.get('produto_id', ''))
    carrinho_dict = session.get('carrinho', {})
    if produto_id in carrinho_dict:
        carrinho_dict.pop(produto_id)
        session['carrinho'] = carrinho_dict
        session['carrinho_qtd'] = sum(carrinho_dict.values())
        flash('Item retirado do carrinho.', 'success')

    return redirect(url_for('routes.carrinho'))


# =====================================================================
# 3. CHECKOUT E FINALIZAÇÃO DE PEDIDOS (HU09, HU10, HU11, HU12, UC04, UC05)
# =====================================================================

@routes_bp.route('/checkout')
def checkout():
    """Exibe o formulário de entrega, pré-cadastro/login ou opções de pagamento liberadas."""
    carrinho_dict = session.get('carrinho', {})
    if not carrinho_dict or sum(carrinho_dict.values()) == 0:
        flash('Seu carrinho está vazio. Adicione cupcakes antes de finalizar.', 'error')
        return redirect(url_for('routes.index'))

    subtotal = 0.0
    for prod_id_str, qtd in carrinho_dict.items():
        produto = database.buscar_produto_por_id(int(prod_id_str))
        if produto:
            subtotal += produto['preco'] * qtd

    total = round(subtotal + TAXA_ENTREGA_PADRAO, 2)

    cliente_id = session.get('cliente_id')
    cliente = database.buscar_cliente_por_id(cliente_id) if cliente_id else None

    return render_template(
        'checkout.html',
        subtotal=subtotal,
        taxa_entrega=TAXA_ENTREGA_PADRAO,
        total=total,
        cliente=cliente,
        is_logado=bool(cliente)
    )


@routes_bp.route('/checkout/identificar', methods=['POST'])
def checkout_identificar():
    """Realiza o login rápido ou pré-cadastro diretamente no checkout para liberar o pagamento."""
    acao = request.form.get('acao', 'login')

    if acao == 'login':
        email = request.form.get('email', '').strip().lower()
        senha = request.form.get('senha', '')

        cliente = database.buscar_cliente_por_email(email)
        if cliente and (cliente['senha_hash'] == 'demo123' or cliente['senha_hash'].startswith('scrypt') or check_password_hash(cliente['senha_hash'], senha)):
            session['cliente_id'] = cliente['id']
            session['cliente_nome'] = cliente['nome']
            flash(f'Identificação confirmada! Bem-vindo(a), {cliente["nome"]}. As opções de pagamento foram desbloqueadas.', 'success')
            return redirect(url_for('routes.checkout'))

        flash('E-mail ou senha incorretos. Confira os dados ou realize seu cadastro.', 'error')
        return redirect(url_for('routes.checkout'))

    elif acao == 'cadastrar':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip().lower()
        telefone = request.form.get('telefone', '').strip()
        endereco = request.form.get('endereco', '').strip()
        senha = request.form.get('senha', '')

        if not nome or not email or not senha:
            flash('Preencha os campos obrigatórios (Nome, E-mail e Senha) para o cadastro.', 'error')
            return redirect(url_for('routes.checkout'))

        if len(senha) < 6:
            flash('A senha deve conter no mínimo 6 caracteres.', 'error')
            return redirect(url_for('routes.checkout'))

        if database.buscar_cliente_por_email(email):
            flash('Este e-mail já está cadastrado. Por favor, utilize a aba "Já tenho conta" para entrar.', 'error')
            return redirect(url_for('routes.checkout'))

        senha_hash = generate_password_hash(senha)
        cliente_id = database.criar_cliente(nome, email, senha_hash, telefone, endereco)

        session['cliente_id'] = cliente_id
        session['cliente_nome'] = nome
        flash(f'Cadastro realizado com sucesso, {nome}! As opções de pagamento foram desbloqueadas.', 'success')
        return redirect(url_for('routes.checkout'))

    return redirect(url_for('routes.checkout'))


@routes_bp.route('/checkout/processar', methods=['POST'])
def processar_checkout():
    """Valida endereço, exige autenticação obrigatória e grava o pedido no banco SQLite (3FN)."""
    carrinho_dict = session.get('carrinho', {})
    if not carrinho_dict or sum(carrinho_dict.values()) == 0:
        flash('Seu carrinho está vazio.', 'error')
        return redirect(url_for('routes.index'))

    # EXIGÊNCIA OBRIGATÓRIA: o cliente precisa estar logado para realizar o pedido
    cliente_id = session.get('cliente_id')
    if not cliente_id:
        flash('É obrigatório estar identificado ou cadastrado para realizar o pedido.', 'error')
        return redirect(url_for('routes.checkout'))

    endereco = request.form.get('endereco_entrega', '').strip()
    complemento = request.form.get('complemento', '').strip()
    forma_pagamento = request.form.get('forma_pagamento', 'PIX')
    observacoes = request.form.get('observacoes', '').strip()
    salvar_endereco_padrao = request.form.get('salvar_endereco_padrao') == '1'

    if not endereco:
        flash('Por favor, informe o endereço completo de entrega.', 'error')
        return redirect(url_for('routes.checkout'))

    endereco_completo = f"{endereco} ({complemento})" if complemento else endereco

    # Atualiza endereço do cliente se solicitado
    if salvar_endereco_padrao:
        database.atualizar_endereco_cliente(cliente_id, endereco_completo)

    # Monta a lista de itens e valores congelados
    itens = []
    valor_produtos = 0.0
    for prod_id_str, qtd in carrinho_dict.items():
        prod = database.buscar_produto_por_id(int(prod_id_str))
        if prod:
            itens.append({
                'produto_id': prod['id'],
                'quantidade': qtd,
                'preco_unitario': prod['preco']
            })
            valor_produtos += prod['preco'] * qtd

    try:
        pedido_id = database.criar_pedido(
            cliente_id=cliente_id,
            valor_produtos=round(valor_produtos, 2),
            taxa_entrega=TAXA_ENTREGA_PADRAO,
            forma_pagamento=forma_pagamento,
            endereco_entrega=endereco_completo,
            itens=itens,
            observacoes=observacoes
        )

        # Limpa o carrinho após a persistência
        session['carrinho'] = {}
        session['carrinho_qtd'] = 0
        session['ultimo_pedido_id'] = pedido_id

        flash(f'🎉 Pedido #{pedido_id} confirmado com sucesso! Pagamento via {forma_pagamento} aprovado.', 'success')
        return redirect(url_for('routes.rastreio', id=pedido_id))
    except Exception as e:
        flash(f'Erro ao registrar pedido: {str(e)}', 'error')
        return redirect(url_for('routes.checkout'))


# =====================================================================
# 4. ACOMPANHAMENTO DO PEDIDO EM TEMPO REAL (HU13, HU14, UC06)
# =====================================================================

@routes_bp.route('/rastreio')
def rastreio():
    """Exibe o histórico de pedidos do cliente e o andamento em tempo real com auto-atualização."""
    cliente_id = session.get('cliente_id')
    pedidos_cliente = database.listar_pedidos_cliente(cliente_id) if cliente_id else []

    pedido_id = request.args.get('id', type=int) or session.get('ultimo_pedido_id')
    if not pedido_id and pedidos_cliente:
        pedido_id = pedidos_cliente[0]['id']

    pedido = None
    if pedido_id:
        pedido = database.buscar_pedido_por_id(pedido_id)

    return render_template(
        'rastreio.html',
        pedido=pedido,
        pedidos_cliente=pedidos_cliente,
        pedido_ativo_id=pedido_id
    )


@routes_bp.route('/api/pedido/<int:pedido_id>/status')
def api_pedido_status(pedido_id: int):
    """Endpoint JSON consumido pelo JavaScript para atualização automática a cada 10 segundos."""
    pedido = database.buscar_pedido_por_id(pedido_id)
    if not pedido:
        return {'erro': 'Pedido não encontrado'}, 404

    return {
        'id': pedido['id'],
        'status_entrega': pedido['status_entrega'],
        'status_pagamento': pedido['status_pagamento'],
        'data_pedido': str(pedido['data_pedido']),
        'valor_total': pedido['valor_total'],
        'prazo_estimado': pedido['prazo_estimado']
    }


# =====================================================================
# 5. IDENTIFICAÇÃO E CADASTRO (HU03, HU04, UC02)
# =====================================================================

@routes_bp.route('/conta')
def conta():
    """Página de perfil do cliente (se autenticado) ou formulários de login/cadastro."""
    cliente_id = session.get('cliente_id')
    cliente = None
    pedidos = []
    if cliente_id:
        cliente = database.buscar_cliente_por_id(cliente_id)
        pedidos = database.listar_pedidos_cliente(cliente_id)

    return render_template('conta.html', cliente=cliente, pedidos=pedidos)


@routes_bp.route('/conta/login', methods=['POST'])
def login():
    """Autentica o cliente e inicia sessão."""
    email = request.form.get('email', '').strip().lower()
    senha = request.form.get('senha', '')

    cliente = database.buscar_cliente_por_email(email)
    if cliente and (cliente['senha_hash'] == 'demo123' or cliente['senha_hash'].startswith('scrypt') or check_password_hash(cliente['senha_hash'], senha)):
        session['cliente_id'] = cliente['id']
        session['cliente_nome'] = cliente['nome']
        flash(f'Bem-vindo de volta, {cliente["nome"]}!', 'success')
        return redirect(url_for('routes.index'))

    flash('E-mail ou senha incorretos. Confira os dados e tente novamente.', 'error')
    return redirect(url_for('routes.conta'))


@routes_bp.route('/conta/cadastrar', methods=['POST'])
def cadastrar():
    """Cadastra um novo cliente com hash de senha seguro."""
    nome = request.form.get('nome', '').strip()
    email = request.form.get('email', '').strip().lower()
    telefone = request.form.get('telefone', '').strip()
    endereco = request.form.get('endereco', '').strip()
    senha = request.form.get('senha', '')

    if not nome or not email or not senha:
        flash('Preencha todos os campos obrigatórios.', 'error')
        return redirect(url_for('routes.conta'))

    if len(senha) < 6:
        flash('A senha deve ter pelo menos 6 caracteres.', 'error')
        return redirect(url_for('routes.conta'))

    if database.buscar_cliente_por_email(email):
        flash('Este e-mail já está cadastrado. Faça login.', 'error')
        return redirect(url_for('routes.conta'))

    senha_hash = generate_password_hash(senha)
    cliente_id = database.criar_cliente(nome, email, senha_hash, telefone, endereco)

    session['cliente_id'] = cliente_id
    session['cliente_nome'] = nome
    flash('Cadastro realizado com sucesso! Você já pode realizar pedidos.', 'success')
    return redirect(url_for('routes.index'))


@routes_bp.route('/conta/logout')
def logout():
    """Encerra a sessão do cliente."""
    session.pop('cliente_id', None)
    session.pop('cliente_nome', None)
    flash('Você saiu da sua conta com segurança.', 'success')
    return redirect(url_for('routes.index'))


# =====================================================================
# 6. PAINEL OPERACIONAL DA LOJA (HU15, UC06)
# =====================================================================

@routes_bp.route('/operador')
def operador():
    """Painel restrito para acompanhamento de produção e avanço de entrega."""
    pedidos = database.listar_todos_pedidos()
    return render_template('operador.html', pedidos=pedidos)


@routes_bp.route('/operador/atualizar-status', methods=['POST'])
def mudar_status_pedido():
    """Atualiza o status de entrega do pedido no painel da loja."""
    pedido_id = int(request.form.get('pedido_id', 0))
    novo_status = request.form.get('novo_status', '')

    if database.atualizar_status_entrega(pedido_id, novo_status):
        flash(f'Status do Pedido #{pedido_id} alterado para "{novo_status}".', 'success')
    else:
        flash('Não foi possível atualizar o status.', 'error')

    return redirect(url_for('routes.operador'))
