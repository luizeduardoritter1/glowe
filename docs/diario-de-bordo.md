# 📓 Diário de Bordo — Glowe

Registro do processo de construção do projeto, para aprendizado e portfólio.

---

## [21/07/2026] — Sprint 0: Fundação

**O que fiz hoje**
- Verifiquei o ambiente (git, gh(traz recursos do site do github para o terminal)) e configurei a identidade no git.
- Troquei a branch master por main(padrão atual);
- fiz o primeiro commit e criei o README do projeto;
- Publiquei o repositório no github;
- montei o kanban no GitHub Projects com o backlog inicial e fechei a sprint 0
- decidi usar Django na arquitetura pra construir o backend.

**O que aprendi**
 git config --global user.name e git config --global user.email -> para verificar se já havia conexão com alguma conta.
 git --version -> Verifica a versão instalada
 gh --version -> Verifica a versão instalada
 gh auth status → diz se você está logado no GitHub pelo terminal (ou não).
 git config --global init.defaultBranch main -> ja cria main por padrão nos próximos projetos.
 gh repo create glowe --public --source=. --remote=origin --push
Decifrando cada parte:
- glowe → o nome do repositório;
- --public → Torna o repositório público;
- --source=. → usa esta pasta como origem;
- --remote=origin → apelida a conexão de origin;
- --push → já envia seus commits pra lá.

 Aprendi o modelo das 3 áreas (working → staging → commit) e o ciclo add → commit → push;

**Dificuldades / como resolvi**
Quando fui dar o comando 'gh issue close' esqueci de referenciar a issue que eu estava querendo fechar, então corrigi o comando que estava errado e deu certo. :D

**Decisões**
Decidi por stack web-first com backend em python; Kanban no github projects;

**Próximos passos**
- Configurar o ambiente Python (venv)
- criar o projeto Django
