# Planejamento da loja de cupcakes gourmet

> Atualizado em 26/10/2026. Versão alinhada ao PIT I e ampliada para os requisitos do PIT II. Contém escopo, catálogo de produtos, parâmetros operacionais, histórias de usuário, backlog, casos de uso expandidos e definições da stack tecnológica. [Registro do projeto](README.md#registro).

---

## 1. Escopo e fontes

A proposta é desenvolver uma aplicação Web para uma loja especializada em cupcakes artesanais e gourmet, viabilizando o catálogo virtual, montagem e edição de carrinho, cadastro e login de clientes, checkout com endereço e cálculo de frete, pagamento demonstrativo e acompanhamento da entrega em tempo real, além de um módulo restrito para a gestão operacional dos pedidos.

**Fontes oficiais consultadas:**
- `PITESoftwareI.pdf`, páginas 27–49 (conceitos, histórias, diagramas e mapas);
- `PIT_atividade.docx` (proposta de planejamento inicial);
- `PITESoftwareII.pdf`, páginas 30–40 (desafios complementares e orientações de desenvolvimento e testes);
- [Modelo oficial de entrega II](https://bb.cruzeirodosulvirtual.com.br/bbcswebdav/xid-155446528_1).

---

## 2. Parâmetros Comerciais e Catálogo de Produtos

### 2.1. Catálogo Oficial (5 Sabores)

| ID | Sabor do Cupcake | Descrição dos Ingredientes e Cobertura | Preço Unitário |
|:---:|---|---|:---:|
| 1 | **Chocolate** | Massa fofinha de cacau nobre 100%, recheio cremoso de ganache de chocolate meio amargo e cobertura generosa de brigadeiro tradicional gourmet com granulado belga. | R$ 13,00 |
| 2 | **Ninho com Brigadeiro** | Massa amanteigada de baunilha, recheio generoso de leite Ninho cremoso e cobertura dupla com brigadeiro tradicional e brigadeiro de Ninho. | R$ 14,00 |
| 3 | **Ninho com Morango** | Massa leve de baunilha, recheio de geleia artesanal de morangos frescos e cobertura aveludada de mousse de leite Ninho finalizada com morango fresco. | R$ 15,00 |
| 4 | **Nutella** | Massa de cacau nobre, recheio puro de creme de avelã Nutella e cobertura de brigadeiro de Nutella com finalização em avelãs picadas tostadas. | R$ 16,00 |
| 5 | **Doce de Leite** | Massa de especiarias suaves com toque de canela, recheio e cobertura generosa de doce de leite caseiro cremoso polvilhado com canela e açúcar. | R$ 13,50 |

### 2.2. Parâmetros de Entrega e Pagamento
- **Prazo de entrega:** 15 a 30 minutos na região de proximidade da loja.
- **Taxa de entrega:** Taxa fixa de R$ 6,00 para pedidos locais.
- **Formas de pagamento suportadas:**
  1. **PIX**: Geração de chave simulada/QR Code demonstrativo com confirmação instantânea.
  2. **Cartão de Crédito**: Validação de dados (número, titular, validade, CVV) com simulação de autorização imediata.

---

## 3. Definição da Stack Tecnológica (Padrão MVC)

Conforme os campos solicitados no modelo oficial de entrega da faculdade:

| Componente | Tecnologia Escolhida | Justificativa Técnica |
|---|---|---|
| **Linguagem do Back-end** | **Python (Framework Flask)** | Indicada no material (p. 34). Flask é leve, aderente ao padrão arquitetural **MVC** (Model-View-Controller) e possui sintaxe limpa e de fácil manutenção. |
| **Banco de Dados** | **SQLite** (`database.db`) | SGBD relacional serverless, de fácil portabilidade e manutenção, em conformidade com a 3FN. Não requer servidores externos pesados. |
| **Front-end** | **HTML5, CSS3 e JavaScript (Vanilla)** | Tecnologias canônicas especificadas no enunciado do PIT II (pp. 33 e 38), garantindo acessibilidade, responsividade e rapidez. |
| **Hospedagem** | **Vercel** (com fallback no Netlify / Render) | Suporte nativo a Serverless Functions em Python, deploy ágil e gratuito para a demonstração pública exigida no PIT II. |
| **Plataforma** | **Web (Navegadores modernos / Mobile-friendly)** | Acesso multiplataforma direto pelo navegador sem necessidade de instalação de aplicativos externos. |
| **Modo de Codificação** | **Tradicional** | Desenvolvimento de código-fonte aberto, estruturado em MVC com rotas, templates e modelos de dados. |

A modelagem de dados detalhada, esquema relacional em 3FN, script executável e dicionário de dados estão documentados em [`Banco_de_Dados.md`](Banco_de_Dados.md) e [`schema.sql`](schema.sql).

---

## 4. Histórias de Usuário (15 Histórias)

| ID | História de usuário | O que precisa funcionar | Regra de funcionamento | Prioridade |
|---|---|---|---|:---:|
| HU01 | Como cliente, quero ver a vitrine para conhecer os 5 sabores disponíveis | Exibir os 5 cupcakes cadastrados com fotos, nomes e preços; alertar se o catálogo estiver indisponível | Exibir somente produtos com disponibilidade ativa (`disponivel = 1`) | 1 |
| HU02 | Como cliente, quero consultar os detalhes do cupcake para decidir o pedido | Abrir modal/seção com ingredientes detalhados, recheio e preço | Usar os dados oficiais cadastrados do produto | 2 |
| HU03 | Como cliente, quero me cadastrar para salvar meus dados de entrega | Aceitar nome, e-mail único, senha e telefone; validar campos obrigatórios | Não permitir e-mails duplicados; senha com no mínimo 6 caracteres | 1 |
| HU04 | Como cliente cadastrado, quero acessar minha conta para agilizar meus pedidos | Autenticar credenciais com feedback visual imediato; manter sessão ativa | Bloquear acesso caso o e-mail ou senha estejam incorretos | 1 |
| HU05 | Como cliente, quero adicionar cupcakes ao carrinho com quantidade ajustável | Adicionar o sabor selecionado na quantidade informada | A quantidade deve ser um número inteiro positivo (mínimo 1) | 1 |
| HU06 | Como cliente, quero consultar o carrinho para conferir itens, subtotais e total | Listar itens, quantidades, subtotais, taxa de entrega de R$ 6,00 e valor final | Calcular automaticamente os valores com base nos preços oficiais | 1 |
| HU07 | Como cliente, quero alterar a quantidade de itens no carrinho | Atualizar o subtotal e o total ao alterar a quantidade | Recusar valores nulos, negativos ou fracionários | 2 |
| HU08 | Como cliente, quero remover um cupcake do carrinho para ajustar a compra | Retirar o item selecionado e recalcular o valor total imediatamente | Se o carrinho esvaziar, exibir mensagem de carrinho vazio | 2 |
| HU09 | Como cliente, quero informar o endereço de entrega na região próxima | Validar campos de rua, número e bairro; informar prazo de 15 a 30 min | Impedir finalização sem endereço completo preenchido | 1 |
| HU10 | Como cliente, quero revisar o resumo completo antes de pagar | Apresentar lista de itens, endereço, taxa de entrega e total geral | Permitir voltar para o carrinho caso queira alterar algo | 1 |
| HU11 | Como cliente, quero confirmar o pedido para formalizar a compra | Gerar número único de pedido e registrar os dados no banco | Não permitir confirmação com carrinho vazio ou dados incompletos | 1 |
| HU12 | Como cliente, quero escolher entre PIX e Cartão de Crédito para pagar | Processar pagamento simulado com resposta de aprovação ou recusa | Marcar pedido como `CONFIRMADO` somente após aprovação | 1 |
| HU13 | Como cliente, quero consultar a situação do pagamento do meu pedido | Exibir status (Pendente, Confirmado ou Recusado) com orientações claras | Vincular a transação exclusivamente ao pedido correspondente | 1 |
| HU14 | Como cliente, quero acompanhar o andamento da minha entrega | Exibir linha do tempo (Recebido → Preparando → Em Rota → Entregue) | Exibir apenas pedidos pertencentes ao cliente autenticado | 1 |
| HU15 | Como atendente/loja, quero visualizar a lista de pedidos e atualizar a entrega | Painel restrito para mudar o status de entrega dos pedidos em tempo real | Exigir autenticação/perfil de operador da loja | 1 |

---

## 5. Afinidade, Backlog e Estimativas de Esforço

As 15 histórias foram agrupadas em 6 épicos por afinidade, com estimativas de Story Points e esforço em horas (obedecendo à diretriz do material I de tarefas entre 2 e 12 horas). Todas as 15 tarefas foram implementadas no código-fonte em padrão MVC (`models/database.py`, `controllers/routes.py`, `templates/`, `static/`):

| Ordem | História | Épico / Afinidade | Tarefa Técnica a Executar | Pontos | Horas Estimadas | Status de Implementação |
|:---:|---|---|---|:---:|:---:|:---:|
| 1 | HU01 | Vitrine | Criar modelo de dados de produtos e template da vitrine com os 5 sabores | 3 | 4h | Concluído |
| 2 | HU02 | Vitrine | Desenvolver visualização de detalhes de cada cupcake com ingredientes | 2 | 3h | Concluído |
| 3 | HU03 | Identificação | Criar formulário de cadastro com validações de e-mail e hash de senha | 3 | 5h | Concluído |
| 4 | HU04 | Identificação | Implementar autenticação de sessão e controle de rotas privadas | 3 | 4h | Concluído |
| 5 | HU05 | Carrinho | Implementar rotas e funções de inserção de itens no carrinho | 2 | 3h | Concluído |
| 6 | HU06 | Carrinho | Desenvolver visualização do carrinho com cálculo de subtotais e taxa fixa | 3 | 4h | Concluído |
| 7 | HU07 | Carrinho | Desenvolver atualização dinâmica de quantidades com validação | 2 | 3h | Concluído |
| 8 | HU08 | Carrinho | Implementar exclusão de itens do carrinho e recálculo automático | 1 | 2h | Concluído |
| 9 | HU09 | Pedido | Criar formulário de endereço de entrega com validação de campos | 2 | 3h | Concluído |
| 10 | HU10 | Pedido | Desenvolver tela de revisão de pedido com resumo financeiro | 2 | 3h | Concluído |
| 11 | HU11 | Pedido | Desenvolver persistência do pedido e de seus itens no banco de dados | 5 | 8h | Concluído |
| 12 | HU12 | Pagamento | Implementar fluxo de pagamento demonstrativo (PIX e Cartão) | 5 | 7h | Concluído |
| 13 | HU13 | Pagamento | Criar tela de confirmação e recibo da transação de pagamento | 2 | 3h | Concluído |
| 14 | HU14 | Entrega | Implementar painel de acompanhamento do status do pedido pelo cliente | 3 | 5h | Concluído |
| 15 | HU15 | Operacional | Desenvolver painel do operador para consulta e atualização de status | 5 | 8h | Concluído |
| **Total** | | | | **43 pts** | **62h** | **100% Concluído** |

---

## 6. Casos de Uso Expandidos

| Caso de Uso | Ator e Pré-condição | Fluxo Principal | Fluxos Alternativos e Exceções |
|---|---|---|---|
| **UC01: Consultar Vitrine e Detalhes** | **Ator:** Cliente visitante ou cadastrado.<br>**Pré-condição:** Sistema online. | 1. O cliente acessa a página inicial.<br>2. O sistema exibe os 5 cupcakes cadastrados com preço e foto.<br>3. O cliente clica em "Ver detalhes".<br>4. O sistema exibe os ingredientes e opções de quantidade. | **1a. Catálogo indisponível:** O sistema exibe mensagem amigável de manutenção.<br>**3a. Produto esgotado:** O sistema exibe o aviso "Indisponível no momento" e desativa o botão de adicionar. |
| **UC02: Autenticar e Cadastrar Cliente** | **Ator:** Cliente.<br>**Pré-condição:** Cliente deseja salvar pedidos. | 1. O cliente informa nome, e-mail, senha e telefone.<br>2. O sistema valida os campos e cria o registro.<br>3. Na autenticação, o cliente digita e-mail e senha.<br>4. O sistema confere as credenciais e inicia a sessão. | **2a. E-mail já cadastrado:** O sistema avisa que o e-mail já existe e sugere o login.<br>**4a. Credenciais inválidas:** O sistema exibe mensagem de erro: "E-mail ou senha incorretos." |
| **UC03: Gerenciar Carrinho de Compras** | **Ator:** Cliente.<br>**Pré-condição:** Produto selecionado. | 1. O cliente define a quantidade e clica em "Adicionar ao carrinho".<br>2. O sistema adiciona o item e recalcula o subtotal.<br>3. O cliente acessa o carrinho para conferir itens, taxa de R$ 6,00 e total.<br>4. O cliente pode alterar quantidades ou remover itens. | **1a. Quantidade inválida (<=0):** O sistema alerta "Informe uma quantidade válida maior que zero".<br>**4a. Carrinho esvaziado:** O sistema exibe mensagem de carrinho vazio e botão para voltar à vitrine. |
| **UC04: Finalizar e Confirmar Pedido** | **Ator:** Cliente autenticado.<br>**Pré-condição:** Carrinho com ao menos 1 item. | 1. O cliente clica em "Avançar para Entrega".<br>2. O cliente informa ou confirma o endereço de entrega.<br>3. O sistema exibe a revisão completa com prazo estimado de 15 a 30 min.<br>4. O cliente clica em "Confirmar Pedido".<br>5. O sistema grava o pedido e redireciona para o pagamento. | **1a. Cliente não autenticado:** O sistema redireciona para o login/cadastro e retorna ao fluxo após autenticação.<br>**2a. Endereço incompleto:** O sistema destaca os campos faltantes e impede o avanço. |
| **UC05: Realizar Pagamento Demonstrativo** | **Ator:** Cliente.<br>**Pré-condição:** Pedido registrado com status Pendente. | 1. O cliente escolhe a forma: PIX ou Cartão de Crédito.<br>2. Para PIX: exibe código copia-e-cola e botão de confirmação.<br>3. Para Cartão: solicita dados do cartão e clica em "Pagar".<br>4. O sistema simula a aprovação, atualiza o status para `CONFIRMADO` e exibe o recibo. | **4a. Simulação de falha/recusa:** Se os dados do cartão forem inválidos, o sistema exibe alerta e permite tentar novamente ou trocar a forma de pagamento. |
| **UC06: Acompanhar Pedido e Gestão da Loja** | **Ator:** Cliente e Operador da loja.<br>**Pré-condição:** Pedido confirmado. | 1. O cliente acessa a tela de acompanhamento e visualiza o status (Recebido → Preparando → Em Rota → Entregue).<br>2. O operador da loja acessa o painel de pedidos.<br>3. O operador seleciona o pedido e avança o status de entrega conforme a produção. | **1a. Pedido inexistente ou de outro cliente:** O sistema bloqueia a visualização e avisa que o pedido não foi localizado.<br>**2a. Operador não autorizado:** O sistema redireciona para a página de login restrita. |

---

## 7. Status do Projeto e Próximos Passos

O ciclo de planejamento, modelagem, desenvolvimento e avaliação de usabilidade foi completado:
1. **Catálogo e regras de negócio:** 5 sabores oficiais definidos, frete fixo de R$ 6,00, prazo de 15 a 30 min e pagamentos PIX/Cartão integrados (Concluído).
2. **Modelagem relacional 3FN:** Banco de dados SQLite estruturado com integridade referencial ativa (`schema.sql` e `database.db`) (Concluído).
3. **Protótipo interativo e aplicação MVC:** Protótipo navegável (`Prototipo.html`) e sistema completo em Python/Flask (`models/database.py`, `controllers/routes.py`, `templates/`, `static/`) com fotos reais e perfil nominal na barra superior (Concluído).
4. **Testes de usabilidade e laudo de qualidade:** Cinco testes com participantes externos realizados, sugestões incorporadas e laudo de qualidade formalizado (Concluído).
5. **Relatório acadêmico oficial:** Documento nos formatos DOCX (`Relatorio_PIT_II_Jonatas_Alves_Rodrigues.docx`) e Markdown (`Relatorio_PIT_II.md`) integralmente preenchido conforme o modelo institucional da faculdade (Concluído).
6. **Deploy e entrega:** Preparação de arquivos para deploy na Vercel (`vercel.json`, `requirements.txt`) e submissão dos arquivos e repositório Git ao final da conferência.
