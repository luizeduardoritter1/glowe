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

- **Fiz uma auto avaliação para medir o quanto aprendi do que fiz até aqui**
💻 Parte 1 — Comandos

1. Você fechou tudo e abriu um terminal novo. Quer rodar o servidor Django. Quais comandos você precisa rodar, na ordem? E por que o primeiro deles é obrigatório?
 - Resposta: O primeiro comando que eu tenho que rodar é: "source venv/bin/activate para startar o ambiente virtual, ele é importante para utilizar as bibliotecas do projeto. depois eu dou um "cd" para a página do backend e startar o servidor com o comando python manage.py runserver.

2. Qual a diferença entre git add e git commit? E o que o git push faz depois dos dois?
 - resposta: git add ele guarda todas as alterações que eu fiz no projeto, git commit salva um hístórico do que foi feito, sendo possivel colocar comentário e o git push é responsável por enviar as alterações para o repositório remoto.

3. Qual a diferença entre makemigrations e migrate? Qual dos dois realmente mexe no banco de dados?
 - resposta: Eu ainda não peguei o conceito tecnico desta questão, mas entendi que o makemigrations é a "receita" e migrate mexe com o banco.

4. Você quer fechar o issue nº 5 deixando um comentário explicando a decisão. Escreva o comando completo.
 - resposta: gh issue close 5 --comment "A issue foi fechada por tal e tal motivo"

---
🐍 Parte 2 — Código

5. No model, qual a diferença entre blank=True e null=True? E por que, num campo de texto, a gente usa só o blank=True?
 - resposta: blank=True serve para deixar campo em branco (string vazia) e null=True permite que o campo receba o valor null. No campo de texto se deixa somente blank=True para não haver conflito com null no banco.

6. O que o método __str__ faz no model? O que apareceria na listagem do admin se você não tivesse escrito ele?
 - resposta: O método dunder __str__ serve para nomear um objeto. Se não tivesse iria aparecer algo como object (1)

7. No admin.py escrevemos from .models import Cliente. O que significa aquele ponto (.) antes de models?
 - resposta: significa que eu estou importando daquela raíz (diretório).

---
🧠 Parte 3 — Conhecimento

8. O arquivo db.sqlite3 está no .gitignore, mas o arquivo de migração 0001_initial.py vai pro Git. Por que essa diferença?
 - resposta: Porque no de.sqlite3 contém dados sensíveis de usuários e no arquivo de migração não.

9. O que é um ambiente virtual (venv) e qual problema ele resolve?
 - resposta: O ambiente virtual é como se fosse uma caixa onde se guarda as bibliotecas e ferramentas para usar no projeto para que não venha conflitar com ferramentas e bibliotecas local.

10. Você rodou makemigrations e apareceu "No changes detected". Quais são as 3 coisas que você deve checar pra descobrir o motivo?
 - resposta: Se o arquvo foi salvo, os outros 2 não me lembro.

---
🎁 Bônus (sobre o produto)

11. A gente decidiu um "modelo híbrido" pro sistema: o agendamento é o "átomo" e o evento é um "contêiner opcional". Explica com suas palavras o que isso significa e por que essa decisão foi tomada.
 - resposta: Escolhemos o modelo hibrido, porque o atomo(agendamento) serve o usuário de maneira mais rapida no agendamento e o evento(container opcional) porque consigo agrupar compromissos dentro dele.


   ==> **Correção** <==
1. ✅ Correto
Perfeito: source venv/bin/activate → cd backend → python manage.py runserver. E o motivo está certo — sem ativar, o Python não acha o Django instalado na caixinha.

---
2. 🟡 Quase — um detalhe conceitual importante

Você acertou o commit e o push. Mas o git add não "guarda" nada — ele separa/seleciona o que vai entrar no próximo commit.

Lembra das 3 áreas? O add só move da bandeja "modificado" para a caixa (staging). Nada foi salvo ainda — se você desligar o PC nesse momento, não existe registro nenhum. Quem salva de verdade é o commit.

▎ Por isso existe o git add arquivo.py (só um) em vez de git add . (tudo): você escolhe o que entra em cada commit. É uma seleção, não um salvamento.

---
3. ✅ Certo na essência! (pode rir, mas você acertou 😄)

Sua intuição está correta. O vocabulário técnico é:
- makemigrations → lê seus models, compara com o que já existe e gera um arquivo Python descrevendo as mudanças. Não toca no banco.
- migrate → executa esses arquivos no banco (roda o SQL de verdade) e anota quais já foram aplicados.

Você entendeu o conceito — só faltava o nome bonito. 👌

---
4. ✅ Correto — comando perfeito, com o número no lugar certo.

---
5. ✅ Correto

Só um refinamento de vocabulário: o blank atua na validação (formulários e admin) e o null atua no banco. E seu motivo pra usar só blank em texto está certíssimo: evita ter dois jeitos de estar vazio.

---
6. ✅ Correto — inclusive usou o termo "dunder". 🎯

---
7. 🟡 Quase — vale corrigir

O ponto não significa "raiz". Ele significa "a mesma pasta/app onde este arquivo está" — é o que se chama import relativo.

Então, dentro de core/admin.py, o from .models import Cliente quer dizer: "do models.py que está aqui na pasta core". Se fosse a raiz do projeto, seria outro caminho. Ponto = aqui, nesta mesma pasta.

---
8. ✅ Correto, mas incompleto

Seu motivo está certo (dados sensíveis) — e existem mais dois:
1. O banco é dado local: cada pessoa/ambiente tem o seu, não faz sentido compartilhar;
2. Em produção usaríamos outro banco (PostgreSQL), então o arquivo local seria inútil lá;
3. Já as migrações são código — todo mundo precisa delas pra montar a estrutura do banco do zero.

▎ Resumo: estrutura vai pro Git, dados não.

---
9. ✅ Correto — explicação clara e com suas palavras. 👏

---
10. 🟡 Você lembrou 1 de 3
1. O banco é dado local: cada pessoa/ambiente tem o seu, não faz sentido compartilhar;
2. Em produção usaríamos outro banco (PostgreSQL), então o arquivo local seria inútil lá;
3. Já as migrações são código — todo mundo precisa delas pra montar a estrutura do banco do zero.

▎ Resumo: estrutura vai pro Git, dados não.

---
9. ✅ Correto — explicação clara e com suas palavras. 👏

---
10. 🟡 Você lembrou 1 de 3

Os três checks são:
1. O app existe? (o startapp foi rodado?)
2. O app está no INSTALLED_APPS?
3. O model está dentro do models.py e o arquivo foi salvo? ← esse você lembrou

▎ 💡 Truque pra memorizar: Existe → Registrado → Salvo.

---
11. ✅ Correto — e vou enriquecer o porquê

Você pegou o "o quê" certinho. O motivo por trás é a rotina da Marina: ela tem dias simples (várias clientes soltas) e dias de evento grande (casamento). Se a gente obrigasse a criar um "evento" pra tudo, o dia a dia ficaria burocrático. Se só tivesse agendamento solto, o casamento viraria bagunça.
O contêiner opcional resolve os dois: simples por padrão, poderoso quando precisa.

📊 Resultado

8 corretas + 3 parciais — resultado muito bom pra quem começou há poucos dias. Os conceitos estão assentando de verdade.

🎯 O que vale reforçar (só 3 coisinhas)

1. git add = selecionar, não salvar (quem salva é o commit)
2. O ponto no import = "mesma pasta/app", não raiz
3. Os 3 checks do "No changes detected": Existe → Registrado → Salvo
---

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
