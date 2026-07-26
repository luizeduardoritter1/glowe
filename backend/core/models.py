from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
    

class ItemCatalogo(models.Model):
    class TipoItem(models.TextChoices):
        SERVICO = 'SERVICO', 'Serviço'
        ADICIONAL = 'ADICIONAL', 'Adicional'

    nome = models.CharField(
        max_length=100,
    )
    tipo = models.CharField(
        max_length=20,
        choices = TipoItem.choices,
        default = TipoItem.SERVICO
    )
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    custo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    duracao_min = models.PositiveIntegerField(blank=True, null=True)
    ocupa_agenda = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    class StatusAgendamento(models.TextChoices):
        AGENDADO = 'AGENDADO', 'Agendado'
        CONCLUIDO = 'CONCLUIDO', 'Concluido'
        CANCELADO = 'CANCELADO', 'Cancelado'

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    evento = models.ForeignKey(
        'Evento',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    itens = models.ManyToManyField(ItemCatalogo, blank=True)
    data_hora = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=StatusAgendamento.choices,
        default=StatusAgendamento.AGENDADO
    )
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_hora']

    def __str__(self):
        return f"{self.cliente.nome} - {self.data_hora.strftime('%d/%m/%Y %H:%M')} - {self.status}"

    @property
    def valor_total(self):
        valor_total = 0
        for item in self.itens.all():
            valor_total += item.preco
        return valor_total

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
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_evento = models.DateField()
    local = models.CharField(max_length=200, blank=True)
    valor_sinal = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_evento']

    def __str__(self):
        return f"{self.nome} - {self.data_evento.strftime('%d/%m/%Y')} - {self.cliente.nome}"
    