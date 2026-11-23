# 🤖 DIO Agent

> Seu mentor com Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar, praticar e planejar a sua carreira.

Você não precisa saber programar nem instalar nada complicado. Em **3 passos**, o seu mentor está pronto para usar.

---

## ✨ Três palavras para começar

- 🧠 **Agente de IA:** um chatbot responde perguntas. Um *agente* vai além: lê, planeja e executa passos para ajudar você a alcançar um objetivo. É a diferença entre alguém que explica o caminho e alguém que caminha junto com você.
- 🖥️ **Harness:** é o programa onde o agente roda. O agente é o mentor, e o harness é a sala onde vocês se encontram. O mesmo mentor atende em salas diferentes, por isso o DIO Agent funciona em vários harnesses.
- 🧩 **Skill:** é uma habilidade do agente, descrita em um guia passo a passo. Você não precisa chamar a skill: o agente percebe o que você precisa e usa a certa sozinho.

Esses e outros termos estão no [Glossário](docs/glossary.md).

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um harness

Recomendamos o **Google Antigravity**, que tem limites de uso generosos para quem está começando. Mas qualquer harness da lista funciona: escolha um e siga a instalação da documentação oficial dele.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://code.claude.com/docs |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

### 2️⃣ Baixe o DIO Agent e abra no harness

Baixe este repositório do jeito mais simples para você:

- **Com Git:** no terminal, rode `git clone https://github.com/digitalinnovationone/dio-agent.git`
- **Sem Git:** no topo desta página, clique no botão verde **Code**, depois em **Download ZIP**, e extraia a pasta.

Depois, abra no harness a pasta do projeto, a que tem o arquivo `AGENTS.md` (pelo Git, ela se chama `dio-agent`; pelo .zip, `dio-agent-main`). O harness lê esse arquivo sozinho, e o agente já sabe quem é: o seu mentor de estudos da DIO.

### 3️⃣ Converse

Fale naturalmente, com as suas palavras. Nas primeiras vezes, vale usar um dos [modelos de prompt](#-modelos-de-prompt) abaixo: quanto mais contexto você dá, melhor o agente ajuda.

---

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda você a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |
| [Análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Avalia segurança de código, sistemas e configurações; orienta correção e validação | "Quero verificar se a configuração SSH do meu servidor está segura." |

A pesquisa na web usa a busca do seu harness. Se ele não tiver busca própria, veja [como conectar o You.com](docs/youcom-mcp.md), que tem uma opção gratuita.

---

## 🛡️ GuardAI: segurança com evidências

Em análises de segurança, o DIO Agent atua também como GuardAI. A especialização foi escolhida para tornar a orientação de segurança defensiva e educacional: estabelecer escopo e autorização, explicar conceitos, apoiar conclusões em evidências e ensinar como validar correções sem transformar hipóteses em fatos.

### Arquivos criados e alterados

Na árvore de trabalho desta especialização:

- **Alterados:** `AGENTS.md` (carregamento da skill e da base de segurança), `agent/persona.md` (papel GuardAI) e este `README.md`.
- **Criados:** `agent/knowledge/security-basics.md` (fundamentos de segurança), `agent/app.py` (exemplo de login parametrizado), `skills/vulnerability-analysis/SKILL.md` (processo, ensino, matriz e evidências), `skills/vulnerability-analysis/README.md` e `laboratorio/teste_login_vulneravel.py` / `laboratorio/teste_login.py` (exemplos antes e depois da correção).

### Iniciar o Hermes na raiz do projeto

Abra um terminal na pasta que contém `AGENTS.md` e inicie a conversa interativa:

```bash
hermes
```

O Hermes precisa estar instalado e configurado. Consulte a documentação oficial na tabela de harnesses acima.

### SQL Injection: exemplos do laboratório

Execute os dois exemplos a partir da raiz do projeto:

```bash
python3 laboratorio/teste_login_vulneravel.py
python3 laboratorio/teste_login.py
```

Os exemplos criam tabelas SQLite em memória (`:memory:`) com dados fictícios. Na execução registrada nesta árvore:

- **Vulnerável:** credenciais válidas e senha incorreta tiveram os resultados esperados; a entrada de SQL Injection reproduziu acesso permitido com senha incorreta (`SQL Injection reproduzida: acesso permitido com senha incorreta`).
- **Corrigido:** credenciais válidas e senha incorreta tiveram os resultados esperados; a mesma entrada foi negada (`SQL Injection bloqueada: acesso negado`).

`agent/app.py` foi inspecionado, mas não foi executado contra uma base SQLite em disco. Os exemplos de `laboratorio/` não exercitam esse arquivo e não demonstram o comportamento de um banco persistente ou de produção.

### Teste da skill de SSH

Os testes foram conversas sobre um cenário hipotético: acesso pela rede privada de casa, autenticação por senha e nenhuma recuperação disponível. Não foi fornecida configuração SSH nem inspecionado um servidor real.

- **Antes do ajuste:** ao perguntar sobre segurança SSH, o agente sugeriu diretamente `sudo sshd -t` e `sudo sshd -T`, sem perguntar sobre exposição, autenticação ou recuperação.
- **Após o ajuste, em nova sessão (relato do usuário):** o agente leu `agent/persona.md`, `skills/vulnerability-analysis/SKILL.md` e `agent/knowledge/security-basics.md`; perguntou primeiro sobre exposição, depois autenticação e recuperação, uma pergunta por vez. No resumo final, manteve o cenário hipotético e não atribuiu vulnerabilidade ou severidade sem evidências.
- **Limitação ainda não retestada:** houve uma imprecisão no resumo: “não há recuperação disponível” virou “recuperação não definida”. A preservação exata desse fato após o último ajuste ainda não foi retestada.

O teste posterior demonstra melhora no comportamento de coleta de contexto e na cautela das conclusões. Essa melhora é distinta da limitação de preservação da formulação sobre recuperação, que continua pendente de reteste.

### Evidências (capturas)

Capturas do projeto e do laboratório SQL:

- [01-hermes-projeto.png](images/01-hermes-projeto.png) — mostra o Hermes lendo `AGENTS.md` e `agent/persona.md` e apresentando o DIO Agent. A captura não demonstra explicitamente o GuardAI.
- [02-analise-inicial-sqli.png](images/02-analise-inicial-sqli.png) — análise estática identifica a interpolação de usuário e senha na consulta de `agent/app.py` como risco de SQL Injection; não mostra execução do código.
- [03-testes-basicos-login.png](images/03-testes-basicos-login.png) — mostra a preparação do teste SQLite em memória com conta fictícia e a verificação sintática; nessa captura, os testes ainda não foram executados.
- [04-sqli-antes-correcao.png](images/04-sqli-antes-correcao.png) — execução da versão vulnerável: a entrada de SQL Injection permite acesso mesmo com senha incorreta.
- [05-sqli-apos-correcao.png](images/05-sqli-apos-correcao.png) — execução após a parametrização: credenciais válidas são aceitas, senha incorreta é negada e a entrada de SQL Injection é bloqueada.

SSH — teste inicial, antes do ajuste:

- [06-guardai-contexto-ssh.png](images/06-guardai-contexto-ssh.png) — o agente sugere verificações locais de SSH e pede suas saídas antes de esclarecer primeiro exposição, autenticação e recuperação. Não mostra comandos executados nem configuração inspecionada.

SSH — nova conversa após o ajuste:

- [07-guardai-contexto-ssh-apos-ajuste.png](images/07-guardai-contexto-ssh-apos-ajuste.png) — o agente começa perguntando se o SSH é acessível pela internet, rede privada/VPN ou apenas localmente; ainda não há inspeção da configuração nem conclusão de segurança.
- [08-guardai-recuperacao-ssh.png](images/08-guardai-recuperacao-ssh.png) — a conversa registra um cenário hipotético em rede privada, autenticação por senha e ausência de console ou outro meio de recuperação definido. Não estabelece que nenhum método alternativo exista nem mostra inspeção de servidor real.

### Matriz qualitativa, abordagem educacional e limites

A matriz qualitativa de probabilidade e impacto foi escolhida para explicar a severidade de forma proporcional às evidências e permitir “não determinado” quando faltam dados, evitando falsa precisão. É uma convenção do projeto, sem equivalência automática com CVSS.

A abordagem educacional complementa a análise: explica conceito, causa e princípio de segurança antes da correção; adapta a linguagem ao estudante; apresenta o objetivo de cada investigação antes dos comandos; justifica recomendações defensivas; usa laboratórios autorizados e estimula pensamento crítico com perguntas de entendimento.

As conclusões se limitam às evidências e aos testes descritos. Os exemplos SQL são didáticos e em memória; o caso SSH é hipotético; nenhum desses testes constitui auditoria completa nem prova de segurança em produção.

---

## 📝 Modelos de prompt

Copie, preencha o que está entre colchetes e envie. Não precisa de formato perfeito: o agente pede mais detalhes se precisar.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos.
- Meu objetivo: [ex: ser dev back-end, concluir um Bootcamp]
- O que quero fazer na DIO: [link ou nome do Bootcamp, Formação, Aceleração ou Carreira]
- O que já tenho: [um plano de ação ou de estudos, se tiver]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou, no Desafio de Projeto, o link do repositório do desafio]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código ou repositório: [cole o código ou o link, se tiver]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
```

**🧭 Caminho AI Builder**

```
Quero escolher meu próximo passo na Carreira AI Builder.
- O que quero construir com IA: [ex: um produto para o meu negócio, um software, agentes que automatizam processos, ainda não sei]
- Minha experiência com programação: [nenhuma, o básico, trabalho com desenvolvimento]
- Meu objetivo: [ex: mudar de carreira, tirar uma ideia do papel]
```

---

## 🔄 Mantenha o DIO Agent atualizado

O DIO Agent evolui com o tempo. Se você usou Git, rode `git pull` no terminal, dentro da pasta (ou peça para o próprio agente rodar). Se baixou o .zip, baixe de novo.

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                Este guia
├── AGENTS.md                Definição do agente (lida pelo harness)
├── CLAUDE.md                Atalho para o Claude Code
├── agent/
│   ├── app.py               Exemplo de login com consulta parametrizada
│   ├── persona.md           A personalidade e o tom do agente
│   └── knowledge/           Conhecimentos sobre DIO e fundamentos de segurança
├── skills/                  Uma pasta por skill, cada uma com o seu SKILL.md
│   └── vulnerability-analysis/
│       ├── SKILL.md         Processo de análise de vulnerabilidades
│       └── README.md        Apresentação da skill
├── laboratorio/
│   ├── teste_login_vulneravel.py  Demonstração didática antes da correção
│   └── teste_login.py            Demonstração didática depois da correção
└── docs/
    ├── glossary.md          Glossário de termos
    └── youcom-mcp.md        Como conectar a busca do You.com
```

---

## 🤝 Contribua

Tem uma ideia de skill? Veja [como criar uma skill](skills/README.md) e abra um pull request.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você nos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀
