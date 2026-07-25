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

    
