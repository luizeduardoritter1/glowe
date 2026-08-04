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

---

## [26/07/2026] — Sprint 1: Modelagem do MVP concluída

**O que fiz hoje**
- Criei o model `ItemCatalogo` (unifiquei serviço e adicional num só cadastro, diferenciados por um campo `tipo`).
- Criei o model `Agendamento` (o "átomo" da agenda), ligado ao Cliente.
- Liguei o Agendamento aos itens (ex: maquiagem + penteado no mesmo atendimento).
- Criei o `valor_total`, que soma o preço dos itens automaticamente.
- Deixei o painel admin mais profissional (colunas, filtro e busca) para o Cliente e o Agendamento.
- Criei o model `Evento` (o "contêiner") e liguei o Agendamento a ele de forma opcional.
- Com isso **fechei a modelagem do MVP**: 4 models (Cliente, ItemCatalogo, Agendamento, Evento) com os 3 tipos de relacionamento.
- Testei tudo pelo painel admin e commitei/pushei cada etapa.

**O que aprendi**
- `DecimalField` para dinheiro (nunca usar `FloatField` pra valor — dá erro de arredondamento). Usa `max_digits` e `decimal_places`.
- `TextChoices`: campo com opções fixas, que vira menu suspenso no admin (`choices=X.choices, default=X.OPCAO`).
- `BooleanField` (verdadeiro/falso) com `default`, e `PositiveIntegerField` (inteiro positivo).
- Estrutura de "caixa dentro de caixa": o `TextChoices` fica aninhado DENTRO do model, e os campos ficam no model — a indentação define o que está dentro de quê.
- `ForeignKey` = relacionamento um-para-muitos (1 cliente → vários agendamentos). A chave fica no lado "muitos".
- `on_delete`: o que fazer com os "filhos" se o "pai" for apagado — `CASCADE` (apaga junto), `PROTECT` (impede), `SET_NULL` (desvincula).
- `ManyToManyField` = muitos-para-muitos (1 agendamento → vários itens, 1 item → vários agendamentos). O Django cria uma "tabela do meio" escondida. Não tem `on_delete`.
- `@property` = método que age como atributo (calcula na hora, não guarda). Não gera migração, porque é lógica Python, não é campo.
- Django shell (`python manage.py shell`) pra testar código; `Model.objects.first()` pega um registro. Se eu mudar o código, preciso reiniciar o shell.
- `ForeignKey` opcional: `null=True, blank=True` + `on_delete=SET_NULL` — é a implementação do modelo híbrido (o agendamento pode ter evento ou não).
- String reference (`'Evento'` entre aspas) pra referenciar um model definido mais abaixo no arquivo.
- Customização do admin: `list_display` (colunas), `list_filter` (filtro lateral), `search_fields` (busca — só campos de texto; o `cliente__nome` com `__` atravessa o relacionamento).
- Git: `git add .` pega da pasta atual pra baixo (melhor rodar na raiz); commit/push funcionam de qualquer pasta. "Changes to be committed" = está na staging, ainda não foi commitado.

**Dificuldades / como resolvi**
- No `ItemCatalogo` esqueci de envolver os campos num `class ItemCatalogo(models.Model)` — tinha colocado tudo dentro do `TextChoices` por engano. Resolvi entendendo a lógica de "caixa dentro de caixa" (indentação).
- Coloquei `choices`/`default` no campo `nome` sem querer — tirei, porque `nome` é texto livre.
- Esqueci o `auto_now_add=True` no `criado_em` do Agendamento — corrigi (gerou uma migração de "alter").
- Tentei escrever o método `valor_total` dentro do shell — aprendi que o código vai no `models.py` (arquivo); o shell serve só pra TESTAR.
- Bug silencioso: escrevi `List_display` com L maiúsculo no admin. O Django não deu erro, só ignorou e não mostrou as colunas. Aprendi que quando algo "não funciona mas não dá erro", devo desconfiar de maiúsculas/digitação.
- Achei que tinha commitado o admin, mas só tinha dado `git add` (estava "staged"). Reforcei o ciclo add → commit → push.

**Decisões**
- Modelo híbrido implementado de verdade: o Agendamento tem um `evento` opcional com `on_delete=SET_NULL` (se o evento for apagado, o agendamento continua e só perde o vínculo).
- Catálogo unificado: serviço e adicional são o mesmo model, diferenciados pelo campo `tipo` e pelo `ocupa_agenda`.

**Próximos passos**
- Sair do admin e fazer o sistema aparecer numa página web de verdade (primeira view + template).

---

## [27/07/2026] — Sprint 1: Primeiras páginas web (views, templates e URLs)

**O que fiz hoje**
- Criei minha primeira view (retornando um texto simples com `HttpResponse`) e configurei as rotas: `core/urls.py` + `include('core.urls')` no `config/urls.py`.
- Evoluí a view pra buscar os clientes do banco e mostrar num template HTML (`render` + context).
- Criei o `base.html` e fiz as páginas herdarem dele (herança de templates).
- Criei a página de listagem de agendamentos.
- Adicionei um menu de navegação no `base.html` pra pular entre Clientes e Agendamentos.

**O que aprendi**
- O fluxo MVT do Django: **URL → View → Template → Navegador**.
- View = função Python que recebe o `request` e devolve uma resposta. `HttpResponse` devolve texto; `render` devolve um template.
- Rotas: `path('rota/', view, name='...')`. Cada app tem seu `urls.py`, e a central (`config/urls.py`) usa `include` pra puxar as rotas do app.
- `render(request, 'core/template.html', context)` — o context é um dicionário que leva os dados do Python pro template.
- Linguagem de template: `{{ variavel }}` **mostra** um valor; `{% for %}`/`{% if %}` **fazem** lógica; `{% empty %}` trata a lista vazia; todo `for`/`if` precisa ser fechado (`{% endfor %}`).
- Templates ficam em `app/templates/app/` (o "sobrenome" com o nome do app evita conflito entre apps).
- Herança de templates: o `base.html` tem os `{% block %}` (buracos); as páginas usam `{% extends %}` e preenchem só os blocks. É o DRY — layout escrito uma vez, usado em todas as páginas.
- Filtro de template com `|` (ex: `{{ agendamento.data_hora|date:"d/m/Y H:i" }}` formata a data).
- Tag `{% url 'nome_da_rota' %}` pra criar links pelo **nome** da rota, em vez de "chumbar" o endereço — se a URL mudar, os links se atualizam sozinhos.
- No template dá pra atravessar relacionamento (`{{ agendamento.cliente.nome }}`) e usar a `@property` (`{{ agendamento.valor_total }}`).
- aprendi a relação reversa: do cliente consigo acessar os agendamentos dele. Usei related_name='agendamentos' pra deixar o acesso legível (cliente.agendamentos), e no template chamei sem parênteses
- Criei o primeiro formulário (ClienteForm com ModelForm). Aprendi o padrão da view: se POST valida e salva, se GET mostra o form vazio. E o {% csrf_token %} que protege o envio. Meu site agora escreve no banco.

**Dificuldades / como resolvi**
- No template de agendamentos, nomeei o block como `content` em vez de `conteudo` (o nome que está no `base.html`). O Django **ignorou silenciosamente** e o conteúdo não apareceu (só o cabeçalho). Aprendi que o nome do block no filho tem que ser **idêntico** ao do pai — é da mesma família do bug do `List_display`: falha silenciosa, sem erro. Já aprendi a desconfiar de nome/digitação quando algo "some" sem dar erro.

**Decisões**
- Usei `{% url %}` com os `name` das rotas em vez de endereços chumbados, pra facilitar a manutenção.

**Próximos passos**
- Criar a página de detalhe do cliente (URL dinâmica com parâmetro `<int:id>` + `get_object_or_404`).
- Depois, mostrar na página do cliente os agendamentos dele (voltar pela relação).

---

## [03/08/2026] — Sprint 2: CRUD completo do Cliente (páginas dinâmicas e formulários)

**O que fiz hoje**
- Criei a página de **detalhe do cliente** (URL dinâmica com `<int:id>`) e transformei o nome na lista em link pra ela.
- Mostrei os **agendamentos do cliente** na página de detalhe, usando a **relação reversa** (`related_name='agendamentos'`).
- Adicionei **comentários explicativos** no código (`models.py`, `views.py`, `urls.py`) pra estudar.
- Criei o **formulário de cadastrar cliente** pelo site (`ClienteForm` com `ModelForm`).
- Adicionei **editar cliente** (Update) reaproveitando o mesmo formulário.
- Adicionei **excluir cliente** (Delete) com página de confirmação.
- Com isso, **completei o CRUD do Cliente** todo pelo site (Create, Read, Update, Delete).

**O que aprendi**
- **URL dinâmica**: `<int:id>` captura um número da URL e passa pra view; `get_object_or_404` busca um objeto pelo id (ou mostra "404 não encontrado" em vez de quebrar).
- **Relação reversa**: com `related_name='agendamentos'` eu acesso `cliente.agendamentos` (no template, sem parênteses). É o caminho inverso da ForeignKey.
- **Comentários**: ótimo pra aprender, mas em código profissional a gente comenta menos — o *porquê*, não o *o quê* (código bom é autoexplicativo).
- **ModelForm**: um formulário que o Django gera a partir do model. O padrão da view é: se `POST` → valida (`is_valid`) e salva (`form.save()`) → `redirect`; se `GET` → mostra o form vazio.
- **`{% csrf_token %}`**: selo de segurança obrigatório em formulários `POST` (protege contra ataque CSRF). Sem ele, dá erro 403.
- **Editar** = mesmo form com `instance=objeto` (no GET vem preenchido, no POST atualiza). Reaproveitei um template só (`form_cliente.html`) mudando o título pelo context.
- **Excluir** = ação destrutiva vai por **POST**, nunca por link/GET (segurança: robôs seguem links e poderiam apagar dados). Uso página de confirmação; `objeto.delete()` apaga do banco.
- `redirect` pode levar argumentos (ex: `redirect('detalhe_cliente', id=cliente.id)`).
- O `CASCADE` na prática: apagar um cliente apaga os agendamentos dele junto.
- Reforcei o padrão: a maioria dos meus erros é **nome que não bate** (template, block, rota, import) — e ler a mensagem de erro entrega a solução.

**Dificuldades / como resolvi**
- `ImportError: cannot import name 'AgendamentoForm'` — importei no `views.py` um formulário que ainda não existia no `forms.py`, e isso quebrou o app inteiro. Aprendi a ler esse erro ("não achei o nome X no arquivo Y") e a só importar o que existe/uso.
- `TemplateDoesNotExist` e `NoReverseMatch` — de novo nome que não batia: a view pedia `detalhe_clientes.html` mas o arquivo era `detalhe_cliente.html`; e a rota estava com `name='detalhe_clientes'` enquanto o template pedia `detalhe_cliente`. Corrigi alinhando tudo no singular.

**Decisões**
- Um único template de formulário (`form_cliente.html`) serve pra **criar e editar**, diferenciado só pelo título passado no context.

**Próximos passos**
- Fazer o CRUD do **Agendamento** (o coração do produto), que traz campos de relacionamento (escolher cliente e itens) e um campo de data/hora.
