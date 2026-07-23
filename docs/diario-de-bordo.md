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

---

## [22/07/2026] — Sprint 1: Backend (setup do Django)

**O que fiz hoje**
- configurei o ambiente virtual (venv)
- instalei Django 6.0.7

**O que aprendi**
- python3 --version -> confere a versão python
- python3 -m venv venv -> Cria a pasta venv/
- source venv/bin/activate -> Ativa o ambiente virtual
- "pip" é o instalador de bibliotecas do Python.
- "pip freeze > requirements.txt" anota as bibliotecas instaladas num arquivo. Por quê? Assim qualquer pessoa (ou eu mesmo em outro PC) recria o ambiente idêntico com um comando.

**Dificuldades / como resolvi**


**Decisões**


**Próximos passos**
- Modelar o banco de dados do MVP.
- Criar versões web das telas.

---

## [23/07/2026] — Sprint 1: continuação: Modelando banco de dados MVP

**O que fiz hoje**
- Criei app 'core'
- criei o model Cliente
- Registrei o cliente no admin
- Criei um superusuário e cadastrei minha primeira cliente pelo painel admin.

**O que aprendi**
- Na pasta backend dei o comando 'python manage.py startapp core para criar o app, depois registrei ele em 'backend/config/settings.py' em INSTALLED_APPS adicionando 'core'
- Método dunder '__init__'
- Aprendi a regra do blank/null. Quando é texto, por convenção utilizo somente o blank(string vazia) e não vai o (null) para evitar conflito no banco, tendo 2 jeitos para estar vazio.
- 'python manage.py makemigrations' para criar as migrations
- Aprendi que o django gera um back-office completo de graça
- O __str__ é o que faz aparecer o nome na listagem, se não apareceria algo como 'Cliente object (1)'

**Dificuldades / como resolvi**
- O makemigrations retornou "no changes detected". Descobri que não havia salvo o model no models.py, por isso não aparecia nada. Foi só eu dar um (ctrl + S) para salvar e executar o comando novamente e deu tudo certo. Com isso aprendi a fazer 3 tipos de validação: Se o app existe, se o app está configurado em INSTALLED_APPS e se o arquivo foi salvo.
- Também descobri que na configuração de apps se utiliza ',' no final, assim quando eu for configurar um novo app não corro o risco de esquecer e quebrar a linha. 
- Na hora de preencher a data de nascimento tentei preencher com o padrão "DD/MM/AAAA" e deu erro, a formatação que usa é
'AAAA-MM-DD'.


**Decisões**


**Próximos passos**
- Criar versões web das telas.
