# Manual de Uso e Instalação — Sweet Cupcake Gourmet

> Projeto Integrador Transdisciplinar em Engenharia de Software II (Turma_001). Aplicação Web desenvolvida em Python/Flask no padrão arquitetural MVC (Model-View-Controller) com banco de dados SQLite (3FN).

---

## 1. Visão Geral da Solução

O **Sweet Cupcake Gourmet** é um sistema completo de e-commerce e gestão operacional para uma confeitaria artesanal. Ele atende aos requisitos do PIT II com:

- **Vitrine**: Exibição dos 5 sabores oficiais de cupcakes gourmet com ingredientes, descrições e preços;
- **Identificação**: Cadastro de clientes e autenticação com hash seguro de senhas;
- **Carrinho de Compras**: Adição, edição de quantidade, exclusão de itens e cálculo em tempo real;
- **Checkout e Pagamento**: Validação de endereço para entrega na região próxima (15 a 30 minutos), taxa fixa de R$ 6,00 e simulação de pagamento via **PIX** ou **Cartão de Crédito**;
- **Acompanhamento do Pedido**: Linha do tempo visual em 4 etapas (*Recebido* ➔ *Em Preparo* ➔ *Em Rota* ➔ *Entregue*);
- **Painel Operacional da Loja**: Módulo restrito para visualização da fila de pedidos e alteração do status de entrega pela equipe.

---

## 2. Requisitos de Sistema e Dependências

### Tecnologias Utilizadas:
- **Linguagem:** Python 3.10+
- **Micro-framework:** Flask 3.0+
- **SGBD:** SQLite 3 (embutido no Python)
- **Front-end:** HTML5 semântico, CSS3 com tokens da `skill_design_jhol` e JavaScript Vanilla.

### Arquivo de Dependências (`requirements.txt`):
```text
Flask==3.0.3
Werkzeug==3.0.3
```

---

## 3. Instruções de Instalação e Execução Local

### Passo 1: Clonar ou acessar o diretório do projeto
```bash
cd "Atividade"
```

### Passo 2: Criar e ativar o ambiente virtual (Recomendado)
- **No Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **No Linux/macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Passo 3: Instalar as dependências
```bash
pip install -r requirements.txt
```

### Passo 4: Executar a aplicação Flask
```bash
python app.py
```

O terminal exibirá a mensagem de confirmação:
```text
🧁 Confeitaria Sweet Cupcake rodando localmente em: http://127.0.0.1:5000
```

Abra o seu navegador de preferência e acesse: **`http://127.0.0.1:5000`**.

---

## 4. Guia Passo a Passo de Utilização do Sistema

### 4.1. Escolha dos Cupcakes na Vitrine
1. Na página inicial (**Vitrine**), navegue pelos 5 sabores disponíveis (*Chocolate, Ninho com Brigadeiro, Ninho com Morango, Nutella e Doce de Leite*).
2. Defina a quantidade desejada no seletor de cada card.
3. Clique em **"Adicionar"**. Uma mensagem amigável confirmará a inclusão do item.

### 4.2. Gerenciando o Carrinho de Compras
1. Clique em **"Carrinho"** no menu superior.
2. Confira a lista de itens, o subtotal de cada produto, a taxa de entrega fixa de **R$ 6,00** e o valor total calculado.
3. Para alterar a quantidade, digite o novo número e clique em **"OK"**.
4. Para remover um item, clique em **"Excluir"**.
5. Clique em **"Avançar para Checkout ➔"**.

### 4.3. Finalização, Endereço e Pagamento
1. Preencha o nome do destinatário e o endereço de entrega na região próxima.
2. Selecione a forma de pagamento:
   - **PIX**: O sistema exibe o código copia-e-cola demonstrativo com aprovação instantânea.
   - **Cartão de Crédito**: Preencha os dados simulados (número do cartão, validade e CVV).
3. Clique em **"Confirmar e Finalizar Pedido ➔"**.

### 4.4. Acompanhamento em Tempo Real
1. O sistema redireciona automaticamente para a tela de **Acompanhamento**.
2. Veja o número do pedido gerado no SQLite, o resumo dos itens comprados e a barra de status de entrega:
   - *1. Recebido* ➔ *2. Em Preparo* ➔ *3. Em Rota* ➔ *4. Entregue*.

### 4.5. Gestão de Pedidos (Área da Loja)
1. Acesse **"Área da Loja"** na barra de navegação.
2. Visualize a listagem completa dos pedidos registrados no banco com nome do cliente, itens e valor.
3. No campo de seleção, altere a etapa de entrega (ex: de *Em Preparo* para *Em Rota*) e clique em **"Atualizar"**.
4. Retorne à tela de **Acompanhamento** para constatar a evolução imediata do status para o cliente.

---

## 5. Arquitetura MVC Implementada

A estrutura física do código respeita estritamente o padrão de separação de responsabilidades:

- **`models/database.py` (Model):** Centraliza as conexões com o SQLite, validação de regras de banco (3FN) e funções de CRUD para clientes, catálogo de cupcakes, pedidos e itens de pedido.
- **`templates/` e `static/` (View):** Templates Jinja2 (`base.html`, `vitrine.html`, `carrinho.html`, etc.) combinados com a folha de estilo `style.css` (tokens da `skill_design_jhol`), garantindo acessibilidade, contraste e responsividade.
- **`controllers/routes.py` e `app.py` (Controller):** Gerenciam as rotas HTTP, requisições GET/POST, sessões de usuário, mensagens flash e orquestram a comunicação entre Model e View.
