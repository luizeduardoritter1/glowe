# models.py — aqui a gente descreve as TABELAS do banco como classes Python.
# Regra de ouro: cada classe (Model) = uma tabela; cada atributo = uma coluna.
# O Django lê este arquivo e cria/atualiza o banco através das migrações.

from django.db import models
from django.urls import reverse


# ═══════════════ CLIENTE ═══════════════
# Guarda os dados de cada cliente atendido.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)            # texto curto (até 100 caracteres)
    telefone = models.CharField(max_length=20)         # texto curto
    email = models.EmailField(blank=True)              # e-mail; blank=True → opcional no formulário
    data_nascimento = models.DateField(blank=True, null=True)  # data; opcional (blank p/ formulário, null p/ banco)
    observacoes = models.TextField(blank=True)         # texto longo, opcional
    criado_em = models.DateTimeField(auto_now_add=True)  # preenche a data/hora sozinho ao criar o registro

    class Meta:
        ordering = ['nome']   # sempre lista os clientes em ordem alfabética de nome

    # __str__ define como o objeto "se apresenta" (no admin, no shell, nas listas).
    def __str__(self):
        return self.nome      # mostra o nome, em vez de "Cliente object (1)"

    def get_absolute_url(self):
        # Para onde as CBVs (Create/Update) redirecionam após salvar.
        return reverse('detalhe_cliente', kwargs={'id': self.id})


# ═══════════════ ITEM DE CATÁLOGO ═══════════════
# Um item vendável: serviço (maquiagem) OU adicional (coffee break). Unificado num model só.
class ItemCatalogo(models.Model):
    # TextChoices = lista de opções fixas pro campo 'tipo' (vira menu suspenso no admin).
    class TipoItem(models.TextChoices):
        SERVICO = 'SERVICO', 'Serviço'         # (valor guardado no banco, rótulo mostrado na tela)
        ADICIONAL = 'ADICIONAL', 'Adicional'

    nome = models.CharField(
        max_length=100,
    )
    tipo = models.CharField(
        max_length=20,
        choices = TipoItem.choices,     # só aceita os valores definidos no TipoItem
        default = TipoItem.SERVICO      # se nada for escolhido, assume "Serviço"
    )
    preco = models.DecimalField(max_digits=8, decimal_places=2)  # dinheiro: use Decimal, NUNCA Float (evita erro de arredondamento)
    custo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # custo (p/ calcular lucro); opcional
    duracao_min = models.PositiveIntegerField(blank=True, null=True)  # duração em minutos; opcional
    ocupa_agenda = models.BooleanField(default=True)  # serviço ocupa horário na agenda? adicional geralmente não
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('detalhe_item', kwargs={'id': self.id})


# ═══════════════ AGENDAMENTO ═══════════════
# O "átomo" da agenda: um atendimento marcado.
class Agendamento(models.Model):
    class StatusAgendamento(models.TextChoices):
        AGENDADO = 'AGENDADO', 'Agendado'
        CONCLUIDO = 'CONCLUIDO', 'Concluido'
        CANCELADO = 'CANCELADO', 'Cancelado'

    # ForeignKey = relação "um-para-muitos": 1 cliente tem vários agendamentos.
    # on_delete=CASCADE → se apagar o cliente, apaga os agendamentos dele junto.
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='agendamentos'
        )

    # Vínculo OPCIONAL com um evento (o "contêiner"). É a implementação do modelo híbrido.
    evento = models.ForeignKey(
        'Evento',                    # 'Evento' entre aspas porque essa classe é definida mais abaixo no arquivo
        on_delete=models.SET_NULL,   # se apagar o evento, o agendamento CONTINUA e só perde o vínculo
        null=True,
        blank=True                   # null + blank = campo opcional
    )

    # ManyToMany = relação "muitos-para-muitos": 1 agendamento tem vários itens,
    # e 1 item pode estar em vários agendamentos. O Django cria uma tabela escondida ("do meio") pra isso.
    itens = models.ManyToManyField(ItemCatalogo, blank=True)

    data_hora = models.DateTimeField()   # data/hora do atendimento (você define — por isso SEM auto_now_add)
    status = models.CharField(
        max_length=20,
        choices=StatusAgendamento.choices,
        default=StatusAgendamento.AGENDADO
    )
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_hora']   # agenda em ordem cronológica

    def __str__(self):
        # f-string monta um texto com variáveis; strftime formata a data bonitinha.
        return f"{self.cliente.nome} - {self.data_hora.strftime('%d/%m/%Y %H:%M')} - {self.status}"

    # @property = um "campo calculado": não guarda no banco, calcula na hora que é chamado.
    # Aqui: soma o preço de todos os itens ligados a este agendamento.
    @property
    def valor_total(self):
        valor_total = 0
        for item in self.itens.all():   # percorre cada item ligado a este agendamento
            valor_total += item.preco   # acumula o preço no total
        return valor_total

    def get_absolute_url(self):
        return reverse('detalhe_agendamento', kwargs={'id': self.id})


# ═══════════════ EVENTO ═══════════════
# O "contêiner opcional": agrupa agendamentos de um trabalho grande (ex: casamento).
class Evento(models.Model):
    class TipoEvento(models.TextChoices):
        CASAMENTO = 'CASAMENTO', 'Casamento'
        ANIVERSARIO = 'ANIVERSARIO', 'Aniversário'
        FORMATURA = 'FORMATURA', 'Formatura'
        ENSAIO = 'ENSAIO', 'Ensaio'
        OUTROS = 'OUTROS', 'Outros'

    nome = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=20,
        choices=TipoEvento.choices,
        default=TipoEvento.OUTROS
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # o cliente principal do evento (ex: a noiva)
    data_evento = models.DateField()
    local = models.CharField(max_length=200, blank=True)            # onde o evento acontece; opcional
    valor_sinal = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # sinal p/ reservar; opcional
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_evento']

    def __str__(self):
        return f"{self.nome} - {self.data_evento.strftime('%d/%m/%Y')} - {self.cliente.nome}"
