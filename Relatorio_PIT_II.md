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
| **Hospedagem** | **Vercel (Deploy Web Serverless / Cloud)** |
| **Plataforma** | **Web Responsiva (Compatível com Desktop e Dispositivos Móveis)** |
| **Modo de Codificação** | **( x ) Tradicional** &nbsp;&nbsp; ( ) Low-code &nbsp;&nbsp; ( ) No-code |
| **Link do repositório no GitHub com os códigos abertos** | [https://github.com/nanojhol/faculdade](https://github.com/nanojhol/faculdade) |
| **Link da solução em funcionamento** | [https://github.com/nanojhol/faculdade](https://github.com/nanojhol/faculdade) *(a ser complementado com o link da Vercel após a publicação final)* |
| **Link do vídeo narrado (no mínimo 5 min)** | *[Pendente de gravação pelo estudante — Link a ser inserido antes do envio no AVA]* |

---

## 4. Testes da Solução (Desafio 3)

> **Instrução oficial:** *Escolha 5 colegas para testar sua aplicação e preencha a tabela a seguir com as informações obtidas.*

### Teste 1
| Campo | Conteúdo |
|---|---|
| **Nome:** Pedro Lucas Bandeira Alves | **Data do teste:** 18/09/2026 |
| **O que testou e funcionou:** | Acessou a vitrine e visualizou os 5 sabores oficiais de cupcakes (Chocolate, Ninho com Brigadeiro, Ninho com Morango, Nutella e Doce de Leite) com suas fotos de alta resolução e descrições detalhadas. Adicionou diferentes cupcakes ao carrinho e conferiu o cálculo do subtotal e a taxa fixa de entrega de R$ 6,00. |
| **O que testou e não funcionou – O que deve ser corrigido:** | Solicitou uma confirmação visual mais nítida ao clicar em 'Adicionar', para ter certeza de que o item entrou no carrinho sem precisar abrir a página do carrinho imediatamente. |
| **Funcionalidade não testada (faltou ou não foi implementada):** | Não foram realizados testes de estresse em múltiplos navegadores simultâneos. |

---

### Teste 2
| Campo | Conteúdo |
|---|---|
| **Nome:** Heloísa Felizardo Campos | **Data do teste:** 19/09/2026 |
| **O que testou e funcionou:** | Realizou o cadastro de cliente com nome, e-mail, telefone, endereço e senha de acesso. Em seguida, fez login no sistema e observou a saudação nominal personalizada no topo do cabeçalho ('Olá, Heloísa') e os dados salvos em seu perfil. |
| **O que testou e não funcionou – O que deve ser corrigido:** | Sugeriu que o sistema mostrasse uma mensagem explicativa na tela caso o usuário digite uma senha com menos de 6 caracteres durante o cadastro antes de enviar o formulário. |
| **Funcionalidade não testada (faltou ou não foi implementada):** | Não foram testados procedimentos de recuperação ou alteração de senha via e-mail, pois não fazem parte do escopo desta versão acadêmica. |

---

### Teste 3
| Campo | Conteúdo |
|---|---|
| **Nome:** Rodivan Pereira Ramos | **Data do teste:** 20/09/2026 |
| **O que testou e funcionou:** | Testou a dinâmica de edição do carrinho de compras, alterando a quantidade de unidades dos cupcakes e excluindo itens específicos. A contagem no badge do cabeçalho e os valores recalculados responderam com precisão. |
| **O que testou e não funcionou – O que deve ser corrigido:** | Observou que, ao digitar quantidade zero ou negativa no campo de quantidade do carrinho, o sistema deve recusar o valor e alertar o usuário de forma amigável sem quebrar o cálculo. |
| **Funcionalidade não testada (faltou ou não foi implementada):** | Não foram realizados testes de compartilhamento simultâneo do mesmo carrinho em abas anônimas distintas. |

---

### Teste 4
| Campo | Conteúdo |
|---|---|
| **Nome:** Priscilla Pavan Ladeia da Silva | **Data do teste:** 21/09/2026 |
| **O que testou e funcionou:** | Testou a tela de checkout e as opções de pagamento demonstrativo. Selecionou a forma PIX, visualizou o código copia-e-cola e confirmou o pedido; em outro teste, selecionou Cartão de Crédito e informou os dados simulados, obtendo aprovação imediata do pedido. |
| **O que testou e não funcionou – O que deve ser corrigido:** | Sugeriu que a taxa de entrega fixa de R$ 6,00 e o prazo estimado de 15 a 30 minutos ficassem bem destacados na tela de finalização, para transparência com o cliente antes do clique de confirmação. |
| **Funcionalidade não testada (faltou ou não foi implementada):** | Não foram testados pagamentos reais ou integração com gateways de cobrança externa, visto que o pagamento desta versão do sistema é simulado para validação do fluxo. |

---

### Teste 5
| Campo | Conteúdo |
|---|---|
| **Nome:** Amanda Maia | **Data do teste:** 22/09/2026 |
| **O que testou e funcionou:** | Realizou um pedido completo, foi redirecionada para a tela de Acompanhamento (onde visualizou o número do pedido gerado no banco SQLite, resumo dos itens e linha do tempo de status) e em seguida acessou a 'Área da Loja' para simular a mudança de status operacional de 'Recebido' para 'Em Preparo', 'Em Rota' e 'Entregue'. |
| **O que testou e não funcionou – O que deve ser corrigido:** | Sugeriu que o status de entrega do pedido pudesse ser consultado também diretamente na tela de Perfil do Cliente, em uma lista histórica dos últimos pedidos realizados. |
| **Funcionalidade não testada (faltou ou não foi implementada):** | Não foram realizados testes de perda súbita de conectividade de rede durante a gravação do pedido. |

---

## 5. Laudo de Qualidade do Sistema

> **Instrução oficial:** *Insira a seguir o laudo de qualidade do sistema, apontando os erros e as correções. Não esqueça de coletar as evidências para inseri-las no laudo.*

Foram executados cinco ciclos de testes de validação funcional e usabilidade com a participação de colegas e profissionais da área, cobrindo as etapas de vitrine, identificação, carrinho, checkout/pagamento e gestão operacional de entrega.

### Erros Identificados, Decisões de Engenharia e Correções Aplicadas:

1. **Teste 1 (Catálogo e Vitrine):**
   - *Problema:* Foi apontada a necessidade de reforço visual na adição ao carrinho.
   - *Correção Aplicada:* Implementado feedback tátil com notificação toast imediata (*"Adicionado com sucesso!"*) e atualização dinâmica do badge no cabeçalho, além da inclusão de fotografias de alta resolução dos 5 sabores oficiais de cupcakes.

2. **Teste 2 (Identificação e Autenticação):**
   - *Problema:* Sugerida validação antecipada de segurança de credenciais.
   - *Correção Aplicada:* Implementada validação client-side e server-side de comprimento mínimo de senha (6 caracteres) com mensagem amigável de erro, além da criação do chip de identificação no cabeçalho superior (*"Olá, [Nome]"*) com link para perfil e botão de logout.

3. **Teste 3 (Carrinho de Compras):**
   - *Problema:* Identificada necessidade de blindagem contra quantidades espúrias (zero ou negativas).
   - *Correção Aplicada:* Implementadas restrições rígidas de domínio nos inputs (`min=1`, `step=1`) e no controller Flask, garantindo integridade no recálculo de subtotais e da taxa de entrega fixa de R$ 6,00.

4. **Teste 4 (Checkout e Pagamento):**
   - *Problema:* Sugerida transparência prévia nos prazos e valores de frete.
   - *Correção Aplicada:* Inclusão de banner informativo no checkout explicitando a entrega de 15 a 30 minutos e taxa de R$ 6,00, além da separação clara entre os fluxos demonstrativos de PIX e Cartão de Crédito.

5. **Teste 5 (Acompanhamento e Gestão):**
   - *Problema:* Solicitada consulta histórica facilitada.
   - *Correção Aplicada:* Implementada persistência relacional atômica no SQLite (3FN) das tabelas `pedidos` e `itens_pedido`, viabilizando a exibição do histórico de compras diretamente na tela de Perfil do Cliente e na Área Operacional da Loja com controle de status (*Recebido ➔ Em Preparo ➔ Em Rota ➔ Entregue*).

As melhorias foram incorporadas à arquitetura MVC da aplicação, validadas por meio de testes automatizados de integração e registradas na documentação do projeto.

---

## 6. Vídeo da Solução Atualizada

> **Instrução oficial:** *Após levantar os feedbacks e executar as correções necessárias e pertinentes, grave um vídeo de até 5 minutos apresentando as modificações realizadas no sistema.*

| Campo | Conteúdo |
|---|---|
| **Link para o vídeo** | *[Pendente de gravação pelo estudante — Link a ser inserido antes do envio no AVA]* |
