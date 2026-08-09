"""
Popula o banco com dados fictícios para testar o sistema.
Uso: python manage.py seed_dados

Clientes e itens do catálogo usam get_or_create (não duplicam ao rodar de novo).
Agendamentos, eventos e lançamentos são recriados a cada execução.
"""
import random
from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import Cliente, ItemCatalogo, Agendamento, Evento, ItemOrcamento, Lancamento


class Command(BaseCommand):
    help = 'Cria dados fictícios (clientes, catálogo, agendamentos, eventos e lançamentos) para teste.'

    def handle(self, *args, **options):
        # ---------- Clientes ----------
        nomes = [
            'Juliana Alves', 'Carla Mendes', 'Beatriz Souza', 'Fernanda Lima',
            'Patrícia Rocha', 'Amanda Costa', 'Larissa Dias', 'Rafaela Nunes',
            'Camila Freitas', 'Bruna Martins', 'Sofia Cardoso', 'Marina Teixeira',
        ]
        tags_opcoes = ['', 'VIP', 'Noiva', 'Indicação', 'VIP, Noiva', 'Fidelidade']
        clientes = []
        for nome in nomes:
            cliente, _ = Cliente.objects.get_or_create(
                nome=nome,
                defaults={
                    'telefone': f'(51) 9 9{random.randint(100, 999)}-{random.randint(1000, 9999)}',
                    'email': nome.split()[0].lower() + '@exemplo.com',
                    'data_nascimento': date(random.randint(1985, 2003), random.randint(1, 12), random.randint(1, 28)),
                    'tags': random.choice(tags_opcoes),
                    'observacoes': random.choice(['', 'Pele sensível.', 'Prefere tons neutros.', 'Alergia a níquel.']),
                },
            )
            clientes.append(cliente)

        # ---------- Catálogo ----------
        servicos = [
            ('Maquiagem social', 220, 60), ('Maquiagem noiva', 350, 90),
            ('Penteado', 250, 60), ('Design de sobrancelha', 80, 30),
            ('Limpeza de pele', 180, 60),
        ]
        adicionais = [
            ('Coffee break', 300, 120), ('Filmagem do preparo', 500, 200),
            ('Brinde personalizado', 90, 40),
        ]
        itens = []
        for nome, preco, dur in servicos:
            it, _ = ItemCatalogo.objects.get_or_create(
                nome=nome, defaults={'tipo': 'SERVICO', 'preco': preco, 'duracao_min': dur})
            itens.append(it)
        for nome, preco, custo in adicionais:
            it, _ = ItemCatalogo.objects.get_or_create(
                nome=nome, defaults={'tipo': 'ADICIONAL', 'preco': preco, 'custo': custo, 'ocupa_agenda': False})
            itens.append(it)
        servicos_qs = [i for i in itens if i.tipo == 'SERVICO']

        # ---------- Agendamentos (de -45 a +25 dias) ----------
        agora = timezone.localtime(timezone.now())
        n_ag = 0
        for _ in range(40):
            dias = random.randint(-45, 25)
            hora = random.choice([9, 10, 11, 14, 15, 16, 17])
            dt = (agora + timedelta(days=dias)).replace(
                hour=hora, minute=random.choice([0, 30]), second=0, microsecond=0)
            ag = Agendamento.objects.create(
                cliente=random.choice(clientes),
                data_hora=dt,
                status='CONCLUIDO' if dias < 0 else 'AGENDADO',
                local=random.choice(['ESTUDIO', 'DOMICILIO']),
            )
            ag.itens.set(random.sample(servicos_qs, random.randint(1, 2)))
            n_ag += 1

        # ---------- Eventos + orçamento ----------
        rotulos = ['Casamento', '15 anos', 'Formatura', 'Ensaio']
        tipos = ['CASAMENTO', 'ANIVERSARIO', 'FORMATURA', 'ENSAIO']
        locais = ['Espaço Green', 'Buffet Estrela', 'Chácara Bela Vista', 'Salão Diamante']
        for i in range(4):
            cli = random.choice(clientes)
            ev = Evento.objects.create(
                nome=f'{rotulos[i]} da {cli.nome.split()[0]}',
                tipo=tipos[i],
                cliente=cli,
                data_evento=date.today() + timedelta(days=random.randint(15, 120)),
                local=locais[i],
                valor_sinal=random.choice([300, 500, 800]),
            )
            for it in random.sample(itens, random.randint(2, 4)):
                ItemOrcamento.objects.create(evento=ev, item=it, quantidade=random.randint(1, 3))

        # ---------- Lançamentos (últimos 6 meses) ----------
        despesas = ['Cosméticos', 'Transporte', 'Material descartável', 'Aluguel do espaço', 'Marketing']
        n_lanc = 0
        for _ in range(50):
            d = date.today() + timedelta(days=random.randint(-175, 0))
            if random.random() < 0.65:
                Lancamento.objects.create(
                    descricao=f'Atendimento — {random.choice(nomes).split()[0]}',
                    tipo='RECEITA', valor=random.choice([180, 220, 250, 350, 480]), data=d)
            else:
                Lancamento.objects.create(
                    descricao=random.choice(despesas),
                    tipo='DESPESA', valor=random.choice([80, 120, 200, 340, 600]), data=d)
            n_lanc += 1

        self.stdout.write(self.style.SUCCESS(
            f'Dados fictícios criados: {len(clientes)} clientes, {len(itens)} itens, '
            f'{n_ag} agendamentos, 4 eventos, {n_lanc} lançamentos.'))
