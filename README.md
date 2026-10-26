# Loja de cupcakes

Projeto Integrador II — Engenharia de Software.

Estou preparando uma loja de cupcakes para o Projeto Integrador Transdisciplinar em Engenharia de Software II. Vou continuar a ideia do PIT I: primeiro revisar o planejamento, depois desenvolver o sistema e, por último, testar e corrigir o que for necessário.

A ideia é que o cliente consiga ver os cupcakes, montar o pedido, fazer o pagamento e acompanhar a entrega.

### Atalhos

| Abrir | Conteúdo |
|---|---|
| [Arquivos do projeto](./) | Pasta principal da atividade |
| [Relatório Oficial](Relatorio_PIT_II.md) | Versão completa do relatório com respostas, tabelas e laudo de qualidade |
| [Aplicação Flask](app.py) | Ponto de entrada do sistema no padrão arquitetural MVC |
| [Manual de uso](manual_de_uso.md) | Instruções passo a passo de instalação, configuração e uso |
| [Planejamento](Planejamento.md) | Escopo, 5 sabores oficiais, histórias de usuário, backlog e casos de uso |
| [Banco de dados](Banco_de_Dados.md) | Modelos conceitual e lógico (3FN), script físico e dicionário de dados |
| [Script SQL](schema.sql) | DDL e carga inicial de produtos e clientes no SQLite |
| [Diagramas](Diagramas.drawio) | Casos de uso, classes, sequência, atividades e mapas |
| [Protótipo](Prototipo.html) | Telas, fotos reais dos 5 sabores, perfil no topo e fluxo navegável |
| [Contas de Teste](#contas-teste) | 5 contas de demonstração pré-configuradas no SQLite (senha padrão: `123456`) |
| [Melhorias dos Testes](#melhorias-recentes) | Correções aplicadas com base no feedback dos 5 usuários avaliadores |
| [Etapa atual](#etapa-3) | Relatório oficial e laudo de testes concluídos / Validação final e envio |
| [Ferramentas](#ferramentas) | O que usei e por quê |
| [Registro das etapas](#registro) | O que foi feito e o que falta |

Para ver o protótipo, baixe o arquivo `Prototipo.html` e abra no navegador. No GitHub, esse link abre o código do arquivo. Para rodar a aplicação completa com back-end Python/Flask, siga o `manual_de_uso.md`. Para editar os diagramas, abra `Diagramas.drawio` no Draw.io.

### Ordem do trabalho <a id="ordem"></a>

Vou seguir as três situações propostas pela faculdade. Vou registrar aqui o que fiz em cada parte e marcar como concluído o que já estiver conferido.

#### 1. Revisar o planejamento <a id="etapa-1"></a>

- [x] Consultar o material do PIT I, o material do PIT II e o modelo de entrega.
- [x] Procurar os diagramas, o backlog e os protótipos anteriores.
- [x] Preparar uma versão inicial nova do planejamento, porque os arquivos anteriores não foram localizados.
- [x] Definir os 5 sabores de cupcakes, descrições, preços, taxa fixa de entrega (R$ 6,00) e prazo (15 a 30 min).
- [x] Revisar o escopo, as histórias de usuário, os critérios de aceitação e o backlog com estimativas de esforço.
- [x] Revisar os diagramas UML, mapa conceitual e mapa de navegação.
- [x] Desenvolver o modelo conceitual e o modelo lógico normalizado na Terceira Forma Normal (3FN).
- [x] Executar e documentar o banco de dados físico em SQLite e criar o dicionário de dados completo.
- [x] Atualizar o protótipo com os 5 sabores, cálculo automático do carrinho, checkout e simulação de status.
- [x] Solicitar críticas dos colegas sobre o planejamento revisado e registrar os ajustes pertinentes.
- [x] Concluir o repositório Git com a documentação atualizada e código-fonte aberto.

**Onde estou:** planejamento, regras comerciais, protótipo interativo e modelagem física do banco de dados concluídos.

#### 2. Desenvolver a solução <a id="etapa-2"></a>

- [x] Definir a linguagem do back-end (Python/Flask em MVC), o banco (SQLite), a plataforma (Web), a hospedagem (Servidor Local / Localhost) e o modo tradicional de codificação.
- [x] Desenvolver a estrutura MVC da aplicação em Python/Flask (`models/database.py`, `controllers/routes.py` e `templates/`).
- [x] Desenvolver o front-end responsivo com tokens visuais de confeitaria editorial, fotos reais dos 5 cupcakes e perfil de usuário em destaque no cabeçalho quando logado.
- [x] Integrar a interface, o processamento e o banco de dados SQLite (3FN) com persistência atômica de pedidos.
- [x] Testar o front-end e o back-end e tratar os erros de forma amigável.
- [x] Preparar o manual de uso e reunir as bibliotecas utilizadas (`requirements.txt`).
- [x] Configurar o ambiente de execução local com manual passo a passo (`manual_de_uso.md`) e dependências (`requirements.txt`).
- [x] Disponibilizar o repositório público no GitHub (https://github.com/nanojhol/faculdade).

**Onde estou:** código-fonte MVC completamente funcional, testado e com manual de uso pronto.

#### 3. Testar, corrigir e entregar <a id="etapa-3"></a>

- [x] Realizar e documentar os testes de verificação, validação e integração.
- [x] Preparar o formulário com os campos pedidos pela faculdade.
- [x] Obter os testes de cinco colegas ou profissionais da área.
- [x] Registrar os nomes, o que funcionou, as falhas, as sugestões e o que não foi testado.
- [x] Fazer as correções pertinentes, testar as alterações e atualizar a documentação.
- [x] Preparar o laudo de qualidade com os erros, as correções e as evidências.
- [x] Preencher o modelo oficial de entrega da faculdade (`Relatorio_PIT_II.md` e arquivo DOCX institucional para submissão no AVA).
- [x] Gravar e anexar o Vídeo 1 narrado da solução (V1 — Apresentação Geral do Sistema).
- [x] Gravar e anexar o Vídeo 2 narrado da solução (V2 — Apresentação das Melhorias e Correções).
- [ ] Conferir as instruções de envio no AVA, entregar e guardar o comprovante.

**Ainda falta fazer:** conferência final e submissão da atividade no AVA.

### Contas de Demonstração e Teste <a id="contas-teste"></a>

Para facilitar a avaliação da banca, do professor e dos colegas, o banco de dados SQLite já possui 5 contas de teste cadastradas com histórico real de pedidos associados. Todas utilizam a mesma senha de acesso:

**Senha padrão para todas as contas:** `123456`

| Colega / Usuário Avaliador | E-mail de Acesso | Senha Padrão | Pedidos no Banco | Cenário em Destaque |
|---|---|---|---|---|
| **Pedro Lucas Bandeira Alves** | `pedro.alves@exemplo.com` | `123456` | 3 pedidos | Possui pedido ativo (`RECEBIDO`) para validar o auto-avanço de 10s no Rastreio |
| **Heloísa Felizardo Campos** | `heloisa.campos@exemplo.com` | `123456` | 4 pedidos | Histórico completo de pedidos finalizados com layout de topo em linha única |
| **Rodivan Pereira Ramos** | `rodivan.ramos@exemplo.com` | `123456` | 2 pedidos | Validações de carrinho e domínio numérico sem distorções de frete |
| **Priscilla Pavan Ladeia da Silva** | `priscilla.silva@exemplo.com` | `123456` | 5 pedidos | Pedidos demonstrativos em PIX e Cartão com endereço fixo salvo |
| **Amanda Maia** | `amanda.maia@exemplo.com` | `123456` | 3 pedidos | Testes do ciclo completo e tela zerada limpa quando sem pedidos ativos |

> 💡 **Como testar o Acompanhamento em Tempo Real:** Faça login com `pedro.alves@exemplo.com` (senha `123456`) e clique em **Acompanhamento** no menu superior. O sistema carregará automaticamente o pedido ativo dele e você verá o status avançando a cada 10 segundos (`RECEBIDO` ➔ `EM PREPARO` ➔ `EM ROTA` ➔ `ENTREGUE`) com persistência no banco e notificações flutuantes!

---

### Melhorias Implementadas com Base nos Testes dos Usuários <a id="melhorias-recentes"></a>

A partir dos 5 ciclos de testes de usabilidade e engenharia, foram identificados e solucionados os seguintes pontos críticos:

1. **Adição Assíncrona ao Carrinho sem Redirecionamento (Pedro Lucas):**
   - *Problema:* Clicar em "Adicionar" na vitrine forçava a navegação imediata para a tela de carrinho.
   - *Solução:* Migrado para requisições AJAX (`fetch`), mantendo o cliente na vitrine. O botão exibe animação tátil (`✔ Adicionado!`) por 1.8 segundos, o contador numérico no cabeçalho pulsa e se atualiza na hora, e uma notificação *toast* confirma o cupcake adicionado.

2. **Navbar em Linha Única e Pré-Cadastro no Checkout (Heloísa Felizardo):**
   - *Problema:* Quando o usuário estava logado, o cabeçalho quebrava em duas linhas em janelas convencionais de notebook; além disso, clientes deslogados precisavam sair do carrinho para criar conta.
   - *Solução:* Topo redesenhado com `flex-wrap: nowrap` e chip de usuário compacto (`[👤 Olá, Heloísa | Perfil | Sair]`), mantendo 100% do menu alinhado em linha única horizontal. No Checkout, foram criadas abas integradas de login e pré-cadastro, liberando as opções de pagamento somente após a identificação do cliente.

3. **Validação Rigorosa de Domínio e Cálculo Seguro (Rodivan Pereira):**
   - *Problema:* Vulnerabilidade a inputs zero ou negativos no carrinho.
   - *Solução:* Blindagem com regras `min=1` no front-end e validação defensiva no controller Flask, garantindo integridade no recálculo de subtotais e da taxa fixa de entrega de R$ 6,00.

4. **Proteção de Acesso e Carregamento Automático de Pedido Ativo (Priscilla Pavan):**
   - *Problema:* A rota de acompanhamento ficava aberta a anônimos e não exibia diretamente a compra recente do cliente.
   - *Solução:* Exigência estrita de autenticação em `/rastreio` (visitantes deslogados são redirecionados para login com retorno automático). Ao logar, o sistema detecta se há algum pedido em andamento (`status != ENTREGUE`) e o abre imediatamente com a timeline em tempo real.

5. **Auto-Avanço de 10s no Rastreio e Tela Zerada Inteligente (Amanda Maia):**
   - *Problema:* O acompanhamento exigia que alguém abrisse a Área da Loja para alterar status manualmente, e a tela inicial carregava números de pedidos de testes antigos.
   - *Solução:* Implementado auto-avanço a cada 10 segundos via API REST (`/api/pedido/<id>/status`) persistindo a progressão no SQLite até a entrega final. Ao concluir, o badge luminoso `Ao vivo (10s)` encerra. Se não houver pedidos em andamento, a tela inicial abre limpa/zerada com formulário de consulta para pesquisar pedidos anteriores.

---

### Ferramentas que usei <a id="ferramentas"></a>

| Ferramenta ou formato | Uso no projeto | Por que usei |
|---|---|---|
| Git e GitHub | Versionar os arquivos e manter o registro das etapas | A faculdade pede a documentação e os códigos em um repositório |
| Markdown | Escrever planejamento, backlog, dicionário de dados e manual | Mantém o texto simples, organizado e fácil de consultar no GitHub |
| Formato Draw.io | Preparar os diagramas e os mapas editáveis | O material do PIT I indica essa ferramenta para modelagem de software |
| HTML5 e CSS3 | Estruturar e estilizar a interface do protótipo e da aplicação | Padrões da Web indicados nas orientações da disciplina |
| JavaScript | Demonstrar a dinâmica da vitrine, cálculo do carrinho e fluxo de pedidos | Permite simulação do comportamento interativo diretamente no navegador |
| SQLite | SGBD relacional para armazenamento dos dados em 3FN | Leve, confiável, sem necessidade de servidor externo e de fácil manutenção |
| Python / Flask | Linguagem e micro-framework para o back-end no padrão MVC | Sugerido no material da disciplina por sua clareza estrutural e rapidez |
| Servidor Local (Localhost) | Execução da aplicação Flask em ambiente de desenvolvimento | Permite testes completos, depuração ágil e persistência atômica com SQLite |
| Python-docx | Geração automatizada do relatório acadêmico oficial no padrão do modelo | Garante formatação precisa de tabelas, fontes e estrutura solicitada pela faculdade |

### Registro das etapas <a id="registro"></a>

| Etapa | O que foi feito | Ferramentas e motivo | Próximo passo |
|---|---|---|---|
| Preparação | Consultei os materiais I e II, o modelo de entrega e as orientações da disciplina. Encontrei o formulário anterior, mas não localizei os diagramas, o backlog e os protótipos citados nele | Material oficial e consulta aos arquivos para conferir o que o trabalho pede | Preparar o planejamento novo com base no mesmo escopo |
| Planejamento inicial | Organizei 15 histórias de usuário, critérios de aceitação, backlog e casos de uso | Markdown para registrar o conteúdo de forma simples | Revisar as regras, as prioridades e as estimativas pendentes |
| Diagramas e protótipo iniciais | Preparei seis diagramas editáveis e um protótipo das telas. Conferi se o protótipo adiciona e remove o item do carrinho e avisa quando faltam dados | Formato Draw.io para diagramas; HTML, CSS, JavaScript e navegador para as telas | Revisar os diagramas no editor e detalhar o modelo dos dados |
| Organização no Git | Vinculei esta pasta ao repositório faculdade, preservando o commit inicial. Acrescentei atalhos, a ordem das etapas e os motivos das ferramentas usadas | Git e GitHub para acompanhar as versões | Continuar a revisão do planejamento |
| Revisão do texto | Revisei o README, o planejamento e os textos das telas para deixar a leitura mais simples. Mantive as pendências e o escopo da atividade | Markdown, textos do HTML e rótulos do Draw.io para organizar a apresentação | Definir os produtos, as regras de negócio e a modelagem de dados |
| Definição comercial e banco de dados | Defini os 5 sabores de cupcakes, descrições, preços, taxa fixa de R$ 6,00 e prazo de 15 a 30 min. Elaborei os modelos conceitual e lógico (3FN), executei o script físico em SQLite e criei o dicionário de dados. Atualizei o protótipo com os 5 sabores e cálculo real | SQLite, SQL (schema.sql), Markdown e HTML/CSS/JS para viabilizar a estrutura de dados e regras antes da codificação | Iniciar a estrutura da aplicação MVC em Python/Flask |
| Desenvolvimento MVC e aprimoramento visual | Implementei a aplicação completa em padrão MVC (`models/database.py`, `controllers/routes.py`, `templates/`, `static/`), integrei fotos reais nos cards dos 5 cupcakes, destaquei o perfil do usuário logado na barra superior, criei a tela de perfil de cliente e elaborei o manual de uso | Python, Flask, Jinja2, SQLite, CSS com direção de arte editorial de confeitaria e Markdown | Preparar deploy e testes da solução |
| Relatório oficial e laudo de testes | Elaborei o relatório completo de entrega da atividade contendo as tabelas de codificação, os 5 testes de usabilidade com participantes, o laudo de qualidade com correções comprovadas e o manual de execução | Python-docx, Markdown e Microsoft Word para formatação rigorosa no modelo institucional | Validação final de entrega e submissão no AVA |
| Melhorias de Usabilidade e Homologação | Implementei o auto-avanço de 10s no rastreio, carrinho assíncrono via AJAX, pré-cadastro no checkout, layout de navbar em linha única e criei as 5 contas de teste no SQLite (senha `123456`) com pedidos reais sorteados | Python, Flask, SQLite, JavaScript Assíncrono, CSS Flexbox e suite de testes automatizada | Gravação dos vídeos demonstrativos |
| Vídeos Demonstrativos e Fechamento | Gravação dos vídeos narrados da V1 (Apresentação Geral) e da V2 (Melhorias e Correções), com integração direta de ambos os links no relatório oficial Word e Markdown | Google Drive, OBS Studio / Gravador de Tela, Python-docx e Markdown | Submissão final no AVA |

A cada etapa, vou anotar o que fiz, quais arquivos mexi, a ferramenta que usei e o motivo. Se precisar corrigir alguma coisa, vou registrar a mudança sem apagar o que fiz antes.

### Referências

- Material oficial: `PITESoftwareI.pdf`, principalmente páginas 27–49, e `PITESoftwareII.pdf`, páginas 30–40, consultados no acervo da disciplina.
- [Modelo oficial da entrega II](https://bb.cruzeirodosulvirtual.com.br/bbcswebdav/xid-155446528_1).
- [Exemplo consultado — zorkind/cupcake-store](https://github.com/zorkind/cupcake-store): usado somente como referência de organização. Não copiei seu código nem adotei suas ferramentas.
