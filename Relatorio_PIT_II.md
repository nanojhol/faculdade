# Relatório de Entrega — Projeto Integrador Transdisciplinar em Engenharia de Software II

> Modelo Oficial de Entrega do PIT II preenchido conforme as solicitações da disciplina e do AVA. Documento oficial em formato Word preparado para submissão direta no AVA.

---

## 1. Identificação do Estudante

- **Nome:** Jonatas Alves Rodrigues
- **RGM:** [Disponibilizado no relatório oficial enviado ao AVA]
- **Curso:** Engenharia de Software
- **Semestre:** 8º Semestre (Segundo Semestre de 2026)
- **Disciplina:** Projeto Integrador Transdisciplinar em Engenharia de Software II (Turma_001)

---

## 2. Documentação do Projeto (Desafio 1)

> **Instrução oficial:** *Revisite a documentação do projeto desenvolvido na PIT I, faça as atualizações e melhorias necessárias de acordo com os pontos explicitados no material teórico. Ao terminar os ajustes, suba a documentação em um repositório GIT.*

- **Link do Repositório Git:** [https://github.com/nanojhol/faculdade](https://github.com/nanojhol/faculdade)

### Resumo das Atualizações e Revisões Realizadas:
1. **Escopo e Catálogo Oficial de Sabores:** Definição dos 5 sabores gourmet da confeitaria artesanal (*Chocolate*, *Ninho com Brigadeiro*, *Ninho com Morango*, *Nutella* e *Doce de Leite*), descrições de ingredientes e preços unitários.
2. **Parâmetros Operacionais:** Taxa de entrega fixa local de R$ 6,00 e prazo de entrega estimado de 15 a 30 minutos na região de proximidade.
3. **Histórias de Usuário e Backlog:** 15 histórias de usuário (HU01 a HU15) estruturadas com critérios de aceitação, regras de negócio e estimativas de esforço (62 horas / 43 Story Points).
4. **Casos de Uso Expandidos (UML):** 6 casos de uso detalhados (UC01 a UC06) com fluxos principais, alternativos e de exceção, acompanhados de diagramas editáveis no padrão Draw.io (`Diagramas.drawio`).
5. **Modelagem de Dados Relacional (3FN):** Projeto conceitual e lógico formalizado na Terceira Forma Normal, com scripts físicos DDL e carga DML executados no SQLite (`schema.sql` e `database.db`) e **Dicionário de Dados** completo em [`Banco_de_Dados.md`](Banco_de_Dados.md).
6. **IHC e Protótipo Interativo:** Protótipo navegável em HTML5/CSS3/JavaScript com direção visual de confeitaria editorial baseada na `skill_design_jhol` (`Prototipo.html`).

---

## 3. Codificação da Solução (Desafio 2)

> **Instrução oficial:** *Na tabela a seguir insira as informações referentes ao desenvolvimento do código do front-end e back-end.*

| Campo | Conteúdo Oficial Preenchido |
|---|---|
| **Linguagem do Back-end** | **Python (Framework Flask — Padrão Arquitetural MVC)** |
| **Banco de Dados** | **SQLite (Normalizado na Terceira Forma Normal — 3FN)** |
| **Hospedagem** | **Servidor Local / Localhost (Execução em ambiente de desenvolvimento Python/Flask com SQLite)** |
| **Plataforma** | **Web Responsiva (Compatível com Desktop e Dispositivos Móveis)** |
| **Modo de Codificação** | **( x ) Tradicional** &nbsp;&nbsp; ( ) Low-code &nbsp;&nbsp; ( ) No-code |
| **Link do repositório no GitHub com os códigos abertos** | [https://github.com/nanojhol/faculdade](https://github.com/nanojhol/faculdade) |
| **Link da solução em funcionamento** | [https://github.com/nanojhol/faculdade](https://github.com/nanojhol/faculdade) *(Código aberto completo com manual de execução local e protótipo interativo)* |
| **Link do vídeo narrado (no mínimo 5 min)** | [https://drive.google.com/file/d/12bklwOwWQj-rv4l9tdy3alV2JBYcRW6Z/view?usp=sharing](https://drive.google.com/file/d/12bklwOwWQj-rv4l9tdy3alV2JBYcRW6Z/view?usp=sharing) |

---

## 4. Testes da Solução (Desafio 3)

> **Instrução oficial:** *Escolha 5 colegas para testar sua aplicação e preencha a tabela a seguir com as informações obtidas.*

### Contas Homologadas para Testes:
Para facilitar a validação contínua da banca e dos colegas, foram criadas 5 contas no banco de dados SQLite com a senha padrão **`123456`**:

| Colega / Usuário | E-mail de Acesso | Senha Padrão | Pedidos no Banco |
|---|---|---|---|
| **Pedro Lucas Bandeira Alves** | `pedro.alves@exemplo.com` | `123456` | 3 pedidos (1 ativo em preparo) |
| **Heloísa Felizardo Campos** | `heloisa.campos@exemplo.com` | `123456` | 4 pedidos finalizados |
| **Rodivan Pereira Ramos** | `rodivan.ramos@exemplo.com` | `123456` | 2 pedidos finalizados |
| **Priscilla Pavan Ladeia da Silva** | `priscilla.silva@exemplo.com` | `123456` | 5 pedidos finalizados |
| **Amanda Maia** | `amanda.maia@exemplo.com` | `123456` | 3 pedidos finalizados |

---

### Teste 1
| Campo | Conteúdo |
|---|---|
| **Nome:** Pedro Lucas Bandeira Alves | **Data do teste:** 18/10/2026 |
| **O que testou e funcionou:** | Acessou a vitrine e visualizou os 5 sabores oficiais de cupcakes gourmet com fotografias e descrições detalhadas. Adicionou diferentes produtos ao carrinho permanecendo na própria vitrine (sem recarregar ou navegar para fora), observando a animação imediata `✔ Adicionado!` no botão, o incremento no badge do topo e o toast informativo flutuante. |
| **O que testou e não funcionou – O que deve ser corrigido:** | Inicialmente, o sistema redirecionava o usuário para a página do carrinho a cada clique em 'Adicionar', quebrando o fluxo de navegação e escolha dos cupcakes na vitrine. |
| **Funcionalidade não testada (faltou ou não foi implementada):** | Não foram realizados testes de estresse com volume massivo de requisições concorrentes. |

---

### Teste 2
| Campo | Conteúdo |
|---|---|
| **Nome:** Heloísa Felizardo Campos | **Data do teste:** 19/10/2026 |
| **O que testou e funcionou:** | Realizou o fluxo de pré-cadastro e login diretamente pela tela de checkout. Observou o desbloqueio imediato das opções de pagamento após se identificar e notou o cabeçalho superior perfeitamente alinhado em linha única horizontal com o chip de usuário compacto `[👤 Olá, Heloísa \| Perfil \| Sair]`. |
| **O que testou e não funcionou – O que deve ser corrigido:** | Apontou que, ao estar autenticada em resoluções ou janelas convencionais de notebook, os itens da barra de navegação quebravam para uma segunda linha indesejada abaixo da logo, poluindo o topo visual. |
| **Funcionalidade não testada (faltou ou não foi implementada):** | Não foram testados procedimentos de recuperação de senha via SMS ou e-mail transacional externo. |

---

### Teste 3
| Campo | Conteúdo |
|---|---|
| **Nome:** Rodivan Pereira Ramos | **Data do teste:** 20/10/2026 |
| **O que testou e funcionou:** | Testou a manipulação do carrinho de compras e validações de integridade. Verificou o cálculo preciso de subtotais e da taxa fixa de entrega de R$ 6,00 para entrega expressa local em 15 a 30 minutos. |
| **O que testou e não funcionou – O que deve ser corrigido:** | Observou que a digitação de valores inválidos (zero ou negativos) precisava ser tratada e bloqueada tanto no front-end quanto no controller Flask. |
| **Funcionalidade não testada (faltou ou não foi implementada):** | Não foram realizados testes em navegadores legados (versões antigas de Internet Explorer). |

---

### Teste 4
| Campo | Conteúdo |
|---|---|
| **Nome:** Priscilla Pavan Ladeia da Silva | **Data do teste:** 21/10/2026 |
| **O que testou e funcionou:** | Realizou pedidos demonstrativos com pagamento via PIX e Cartão de Crédito. Ao acessar a tela de Acompanhamento, visualizou seu pedido em andamento carregado automaticamente, além de consultar seu histórico completo de compras anteriores na barra lateral. |
| **O que testou e não funcionou – O que deve ser corrigido:** | Sugeriu que a tela de Acompanhamento não ficasse acessível para visitantes anônimos e que, se o usuário não estivesse logado, fosse redirecionado para a tela de login antes de poder pesquisar qualquer pedido. |
| **Funcionalidade não testada (faltou ou não foi implementada):** | Não foi testada a integração com adquirentes financeiras de produção (Stripe/Mercado Pago real). |

---

### Teste 5
| Campo | Conteúdo |
|---|---|
| **Nome:** Amanda Maia | **Data do teste:** 22/10/2026 |
| **O que testou e funcionou:** | Acompanhou a progressão em tempo real de um pedido recém-criado, observando a sincronização automática do status a cada 10 segundos na timeline visual (Recebido -> Em Preparo -> Em Rota -> Entregue) com persistência no SQLite e encerramento do badge 'Ao vivo (10s)' ao entregar. |
| **O que testou e não funcionou – O que deve ser corrigido:** | Apontou que o status ficava estático a menos que alguém abrisse a Área da Loja para alterar manualmente, solicitando que a própria tela de acompanhamento simulasse o avanço contínuo a cada 10 segundos, e que quando todos os pedidos estivessem entregues, exibisse a tela limpa com campo de busca. |
| **Funcionalidade não testada (faltou ou não foi implementada):** | Não foram testadas conexões via WebSockets bidirecionais contínuos (a arquitetura utiliza REST Polling assíncrono de 10s). |

---

## 5. Laudo de Qualidade do Sistema

> **Instrução oficial:** *Insira a seguir o laudo de qualidade do sistema, apontando os erros e as correções. Não esqueça de coletar as evidências para inseri-las no laudo.*

Foram executados cinco ciclos de testes de validação funcional e usabilidade com a participação de colegas e profissionais da área (Pedro Lucas Bandeira Alves, Heloísa Felizardo Campos, Rodivan Pereira Ramos, Priscilla Pavan Ladeia da Silva e Amanda Maia), cobrindo as etapas de vitrine, identificação, carrinho, checkout/pagamento e gestão operacional de entrega em tempo real. Cada usuário possui conta pré-configurada no banco de dados (senha padrão: `123456`) com histórico de pedidos associados.

### Erros Identificados, Decisões de Engenharia e Correções Aplicadas:

1. **Teste 1 (Catálogo e Vitrine — Pedro Lucas):**
   - *Problema Identificado:* O botão 'Adicionar' forçava o redirecionamento imediato para a página do carrinho, quebrando o fluxo de navegação e escolha dos cupcakes.
   - *Correção Aplicada:* Implementada adição assíncrona ao carrinho via fetch/AJAX em `controllers/routes.py` e `static/js/app.js`. O usuário permanece na vitrine, o botão exibe transição tátil `✔ Adicionado!` por 1.8 segundos, o badge de quantidade no cabeçalho é atualizado em tempo real e um toast informativo confirma o item adicionado.

2. **Teste 2 (Identificação e Layout do Topo — Heloísa Felizardo):**
   - *Problema Identificado:* Ao realizar login, a barra de navegação superior sofria quebra de linha ('wrap') devido à largura do chip de usuário e propriedades de flexbox, quebrando a estética visual e o alinhamento do menu.
   - *Correção Aplicada:* Refatoração completa do layout em `static/css/style.css` com `flex-wrap: nowrap`, redução estratégica de paddings e estilização do chip de identificação (`Olá, [Nome] | Perfil | Sair`) em linha única horizontal compacta. Além disso, o Checkout passou a contar com abas integradas de pré-cadastro/login, bloqueando o envio de pedidos anônimos e auto-preenchendo os dados quando autenticado.

3. **Teste 3 (Carrinho e Integridade de Domínio — Rodivan Pereira):**
   - *Problema Identificado:* Possibilidade teórica de inputs com valores zero ou negativos gerarem distorções no recálculo de subtotais e na taxa de entrega.
   - *Correção Aplicada:* Implementação de travas de validação nos níveis client-side (`min=1`, `step=1`) e server-side no controller Flask, garantindo integridade estrita dos valores e cálculo seguro da taxa fixa de R$ 6,00.

4. **Teste 4 (Segurança e Rastreio Inteligente — Priscilla Pavan):**
   - *Problema Identificado:* A tela de Acompanhamento permitia consultas públicas deslogadas e não carregava de forma imediata o pedido ativo que o cliente acabara de solicitar.
   - *Correção Aplicada:* Blindagem da rota `/rastreio` com obrigatoriedade de autenticação. Usuários não autenticados são redirecionados para `/conta?next=rastreio`. Ao efetuar login, o sistema detecta automaticamente se há pedido em andamento (`status != ENTREGUE`) e o exibe de forma destacada, mantendo o histórico de pedidos na barra lateral.

5. **Teste 5 (Acompanhamento em Tempo Real e Auto-Avanço — Amanda Maia):**
   - *Problema Identificado:* A tela de rastreamento dependia exclusivamente da intervenção manual do operador na 'Área da Loja' para mudar de status, não apresentando o dinamismo de avanço temporal esperado em uma demonstração em tempo real.
   - *Correção Aplicada:* Implementado mecanismo de consulta e auto-avanço de etapas a cada 10 segundos via API REST (`/api/pedido/<id>/status`) e JavaScript. O pedido avança dinamicamente: `RECEBIDO` ➔ `EM PREPARO` ➔ `EM ROTA` ➔ `ENTREGUE`, persistindo as mudanças no SQLite. Ao ser finalizado, o badge luminoso `Ao vivo (10s)` encerra e, se não houver outros pedidos em andamento, a tela exibe o estado limpo/zerado com formulário de consulta de pedidos anteriores.

### Conclusão do Laudo de Qualidade:
Todas as 5 solicitações de melhoria foram completamente atendidas, integradas à arquitetura MVC da aplicação, validadas através de testes automatizados de integração com 100% de aprovação e sincronizadas no repositório oficial do projeto.

---

## 6. Vídeo da Solução Atualizada

> **Instrução oficial:** *Após levantar os feedbacks e executar as correções necessárias e pertinentes, grave um vídeo de até 5 minutos apresentando as modificações realizadas no sistema.*

| Campo | Conteúdo |
|---|---|
| **Link para o vídeo** | [https://drive.google.com/file/d/1gABOvdbkX8GcKXJ52Y0FH_O5SLFUSaRq/view?usp=sharing](https://drive.google.com/file/d/1gABOvdbkX8GcKXJ52Y0FH_O5SLFUSaRq/view?usp=sharing) |
