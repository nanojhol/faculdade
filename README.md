# Loja de cupcakes

Projeto Integrador II — Engenharia de Software.

Estou preparando uma loja de cupcakes para o Projeto Integrador Transdisciplinar em Engenharia de Software II. Vou continuar a ideia do PIT I: primeiro revisar o planejamento, depois desenvolver o sistema e, por último, testar e corrigir o que for necessário.

A ideia é que o cliente consiga ver os cupcakes, montar o pedido, fazer o pagamento e acompanhar a entrega.

### Atalhos

| Abrir | Conteúdo |
|---|---|
| [Arquivos do projeto](./) | Pasta principal da atividade |
| [Relatório Oficial (DOCX)](Relatorio_PIT_II_Jonatas_Alves_Rodrigues.docx) | Documento oficial preenchido para entrega da atividade acadêmica |
| [Relatório Oficial (Markdown)](Relatorio_PIT_II.md) | Versão em Markdown com respostas completas e laudo de qualidade |
| [Aplicação Flask](app.py) | Ponto de entrada do sistema no padrão arquitetural MVC |
| [Manual de uso](manual_de_uso.md) | Instruções passo a passo de instalação, configuração e uso |
| [Planejamento](Planejamento.md) | Escopo, 5 sabores oficiais, histórias de usuário, backlog e casos de uso |
| [Banco de dados](Banco_de_Dados.md) | Modelos conceitual e lógico (3FN), script físico e dicionário de dados |
| [Script SQL](schema.sql) | DDL e carga inicial de produtos e clientes no SQLite |
| [Diagramas](Diagramas.drawio) | Casos de uso, classes, sequência, atividades e mapas |
| [Protótipo](Prototipo.html) | Telas, fotos reais dos 5 sabores, perfil no topo e fluxo navegável |
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

- [x] Definir a linguagem do back-end (Python/Flask em MVC), o banco (SQLite), a plataforma (Web), a hospedagem (Vercel) e o modo tradicional de codificação.
- [x] Desenvolver a estrutura MVC da aplicação em Python/Flask (`models/database.py`, `controllers/routes.py` e `templates/`).
- [x] Desenvolver o front-end responsivo com tokens visuais de confeitaria editorial, fotos reais dos 5 cupcakes e perfil de usuário em destaque no cabeçalho quando logado.
- [x] Integrar a interface, o processamento e o banco de dados SQLite (3FN) com persistência atômica de pedidos.
- [x] Testar o front-end e o back-end e tratar os erros de forma amigável.
- [x] Preparar o manual de uso e reunir as bibliotecas utilizadas (`requirements.txt`).
- [x] Configurar o manifesto de hospedagem para a Vercel (`vercel.json`).
- [x] Disponibilizar o repositório público no GitHub (https://github.com/nanojhol/faculdade).

**Onde estou:** código-fonte MVC completamente funcional, testado e com manual de uso pronto.

#### 3. Testar, corrigir e entregar <a id="etapa-3"></a>

- [x] Realizar e documentar os testes de verificação, validação e integração.
- [x] Preparar o formulário com os campos pedidos pela faculdade.
- [x] Obter os testes de cinco colegas ou profissionais da área.
- [x] Registrar os nomes, o que funcionou, as falhas, as sugestões e o que não foi testado.
- [x] Fazer as correções pertinentes, testar as alterações e atualizar a documentação.
- [x] Preparar o laudo de qualidade com os erros, as correções e as evidências.
- [x] Preencher o modelo oficial em formato DOCX e Markdown (`Relatorio_PIT_II_Jonatas_Alves_Rodrigues.docx` e `Relatorio_PIT_II.md`).
- [ ] Conferir as instruções de envio no AVA, entregar e guardar o comprovante.

**Ainda falta fazer:** conferência final e submissão da atividade no AVA.

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
| Vercel | Plataforma de hospedagem para a aplicação Web | Hospedagem ágil e compatível com Serverless Functions em Python |
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
| Relatório oficial e laudo de testes | Elaborei o relatório completo de entrega nos formatos DOCX e Markdown (`Relatorio_PIT_II_Jonatas_Alves_Rodrigues.docx` e `Relatorio_PIT_II.md`), contendo a identificação do estudante (Jonatas Alves Rodrigues, RGM 34733272), as tabelas de codificação, os 5 testes de usabilidade com participantes, o laudo de qualidade com correções comprovadas e o manual de execução | Python-docx, Markdown e Microsoft Word para formatação rigorosa no modelo institucional | Validação final de entrega e submissão no AVA |

A cada etapa, vou anotar o que fiz, quais arquivos mexi, a ferramenta que usei e o motivo. Se precisar corrigir alguma coisa, vou registrar a mudança sem apagar o que fiz antes.

### Referências

- Material oficial: `PITESoftwareI.pdf`, principalmente páginas 27–49, e `PITESoftwareII.pdf`, páginas 30–40, consultados no acervo da disciplina.
- [Modelo oficial da entrega II](https://bb.cruzeirodosulvirtual.com.br/bbcswebdav/xid-155446528_1).
- [Exemplo consultado — zorkind/cupcake-store](https://github.com/zorkind/cupcake-store): usado somente como referência de organização. Não copiei seu código nem adotei suas ferramentas.
