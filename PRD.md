# PRD — Projeto Áurea *(codinome provisório)*
### SaaS de Agenda & Gestão para Profissionais Autônomos da Beleza

> **Product Requirements Document · v0.1 — documento vivo**
> Atualizado: 20/07/2026 · Status: Discovery / Planejamento
> Plataformas: Web · iOS · Android · Persona-foco: **Marina** (maquiadora/penteadista que vai ao cliente)

---

## Sumário
1. [Visão do produto](#1-visão-do-produto)
2. [Análise competitiva — Minha Agenda](#2-análise-competitiva--minha-agenda)
3. [Personas](#3-personas)
4. [Tese & diferenciais](#4-tese--diferenciais)
5. [Escopo do MVP (MoSCoW)](#5-escopo-do-mvp-moscow)
6. [O modelo híbrido](#6-o-modelo-híbrido)
7. [Modelo conceitual](#7-modelo-conceitual)
8. [Catálogo — item unificado](#8-catálogo--item-unificado)
9. [Monetização](#9-monetização)
10. [Roadmap por fases](#10-roadmap-por-fases)
11. [Registro de decisões](#11-registro-de-decisões)
12. [Próximos passos](#12-próximos-passos)

---

## 1. Visão do produto

> **Para** profissionais autônomos da beleza que hoje se viram com caderninho, WhatsApp e planilha,
> **que precisam** enxergar e controlar o negócio inteiro num lugar só,
> **o Projeto Áurea é** um "sócio-gestor de bolso" que organiza a agenda, mostra o dinheiro com clareza e ajuda a atrair cliente —
> **diferente do Minha Agenda**, que é completo mas cobra por tudo e desgasta a confiança do usuário,
> **o nosso** entrega experiência premium, preço honesto e inteligência de verdade.

Essa frase é a **régua** do projeto. Toda decisão de escopo passa por uma pergunta: *isso serve à visão ou é firula?*

> **Princípio norteador:** foco no **usuário profissional**, não no cliente final dele. Não somos um marketplace de beleza — somos a ferramenta de gestão que faz a profissional crescer.

---

## 2. Análise competitiva — Minha Agenda

Concorrente maduro e validado: **4,9★ com ~20 mil avaliações**. O mercado existe e a barra de qualidade é alta. O produto deles é *completo em recursos*, mas *frágil em confiança e confiabilidade* — e é exatamente aí que atacamos.

### O que eles entregam
- **Agenda:** marcar, remarcar, faltas, multa por no-show
- **CRM:** ficha/anamnese, aniversários, "melhores clientes"
- **Comunicação:** lembretes e disparos via WhatsApp
- **Financeiro:** receita, despesa, lucro, metas, comissões, recibos
- **Vendas:** produtos com custo e comissão; fidelidade
- **Plataforma:** iOS, Android, web, tablet; nuvem

### As reclamações = nossas aberturas
| Dor deles | Nossa resposta |
|---|---|
| Paywall agressivo ("tudo é pago") | Free tier honesto + preço justo |
| Reajuste sem cuidado (quebra de confiança) | Preço transparente, sem surpresa |
| Lembrete falha (recurso-chave instável) | Confiabilidade como diferencial |
| Genérico demais (serve "todo mundo") | Desenhado para quem vai ao cliente |

---

## 3. Personas

### Marina — **Beachhead** (foco #1)
Maquiadora / penteadista — **vai até o cliente**. Atende noiva, formanda e eventos no local do cliente. Ticket alto, volume baixo. Negócio em forma de **projeto**, não de horário avulso.
**Precisa de:** orçamento, sinal/depósito, deslocamento, prova + dia vinculados, séquito (noiva + madrinhas).

### Bia — **Fase 2**
Lash / nail / esteticista — **atende no estúdio**. Espaço próprio, agenda cheia de horários curtos e recorrentes. Ticket menor, muito volume.
**Precisa de:** recorrência, pacotes de sessões, controle de no-show, encaixe.

> **Nota:** a rotina real da Marina é **dinâmica** — dias com várias clientes espalhadas, dias com uma só, e dias fechados para um evento grande. Por isso o produto não escolhe entre "agenda simples" e "evento": ele **combina os dois** (ver seção 6).

---

## 4. Tese & diferenciais

Agenda + financeiro + clientes já é *tablestakes* — o concorrente tem. Nosso ganho de jogo está em três frentes:

1. **Confiança** — preço justo e transparente, free tier honesto, lembretes que funcionam. O oposto exato das dores do concorrente.
2. **Feito para quem vai ao cliente** — modelo de **Evento** nativo (orçamento, sinal, prova e dia num só lugar). Nenhum concorrente faz isso bem.
3. **Experiência premium** — padrão internacional de UX: simples por padrão, poderoso sob demanda. A ferramenta que dá orgulho de usar.

---

## 5. Escopo do MVP (MoSCoW)

Meta: núcleo impecável para a Marina, com o **Evento enxuto** como diferencial de lançamento. IA e integrações pesadas ficam para depois — de propósito.

### 🟢 MUST — sem isto, não há produto
- Conta & onboarding (perfil, horário de trabalho, catálogo)
- Agenda: criar/editar/remarcar/cancelar, bloqueios, status
- Clientes (CRM) com histórico e notas
- Catálogo de serviços & adicionais
- Financeiro: receita, despesa, dashboard de faturamento/lucro
- **Evento enxuto:** agrupar agendamentos + orçamento + sinal/saldo
- Orçamento enviável (link/PDF)
- Lembrete semiautomático via WhatsApp (`wa.me`, grátis)

### 🟡 SHOULD — entra se houver fôlego
- Agendamento online (link público)
- Ficha de anamnese rica
- Sincronização com Google Calendar (two-way)

### 🔵 COULD — bom ter, não trava lançamento
- Integração com calendário do iOS (EventKit, no app)
- Metas financeiras
- Cartão fidelidade

### ⚪ WON'T — agora não
- IA de criativo & contrato-IA *(Fase 2)*
- WhatsApp automático (API paga)
- Equipe/colaboradores, comissões, estoque avançado
- Séquito com serviço individual por pessoa

---

## 6. O modelo híbrido

O coração da arquitetura: **o agendamento é o átomo; o Evento é um contêiner opcional.** A complexidade só aparece quando a profissional precisa dela.

**Dia comum →** cria agendamentos soltos. Rápido, três toques, zero cerimônia.
```
Fulana   · qua 15h
Ciclana  · qui 10h
Beltrana · sex 9h
```

**Trabalho grande →** cria um Evento e os agendamentos passam a viver dentro dele.
```
🎉 EVENTO: Casamento da Júlia · 15 nov
   ├─ 📅 Prova · 02 nov · estúdio
   ├─ 📅 Dia   · 15 nov · Gramado
   └─ 💰 R$ 1.800 · sinal R$ 500 ✓ · saldo R$ 1.300
```

> **Custo honesto:** a *arquitetura* híbrida é barata — decidir agora que um agendamento *pode* pertencer a um evento evita reescrever tudo depois. O que é caro é tudo que "pendura" no Evento; por isso o MVP entrega o Evento enxuto e adia séquito rico, contrato-IA e deslocamento automático.

---

## 7. Modelo conceitual

As peças lógicas do sistema e como se conectam (sem código — é o mapa que garante que o Evento nasça certo).

```
                    PROFISSIONAL (a Marina) — é dona de tudo
     ┌───────────────┬─────────────────┬──────────────┐
     │               │                 │              │
  CLIENTE     ITEM DE CATÁLOGO      DESPESA      (config…)
     │        (serviços + adicionais)
     │               │
     └──────► AGENDAMENTO  ◄── o ÁTOMO
              (quando · cliente · itens · local · preço)
                     │
             pode pertencer a ↓ (opcional)
                     │
               EVENTO — contêiner opcional
                 ├─ ORÇAMENTO (lista de itens)
                 └─ PAGAMENTO (sinal / saldo)
```

### As regras de ouro
1. Um **Agendamento** pode viver sozinho *ou* dentro de um Evento. Essa única regra é o coração de tudo.
2. **Orçamento** e **Pagamentos** se prendem ao Evento (casamento) ou direto ao Agendamento (cliente avulsa com sinal).
3. **Item de Catálogo** unifica serviço e adicional — o orçamento é só uma lista deles.
4. Tudo pertence à **Profissional** — dado de uma nunca vaza para outra (base do multi-tenant).

---

## 8. Catálogo — item unificado

Decisão de desenho *(recomendada — em aberto para sua confirmação)*: **um só "Item de Catálogo"** com atributos inteligentes, em vez de separar "serviço" e "produto". Um cardápio só; montar orçamento vira escolher itens da lista.

| Item | Tipo | Preço | Custo | Ocupa agenda? |
|---|---|---|---|---|
| Maquiagem | Serviço | — | — | Sim (tem duração) |
| Penteado | Serviço | — | — | Sim (tem duração) |
| Filmagem | Adicional | R$ X | R$ Y *(repasse à parceira)* | Não |
| Coffee break | Adicional | R$ X | custo dos insumos | Não |

> **Por que assim:** o campo **custo** resolve o caso da filmagem (repasse à parceira) e do coffee break *sem* construir gestão de equipe — o lucro real sai certo. A única diferença funcional entre serviço e adicional é "ocupa tempo na agenda?", resolvida por um atributo.

---

## 9. Monetização

| Etapa | O quê | Detalhe |
|---|---|---|
| **Teste grátis** | 30 dias | Acesso ao núcleo, sem cartão. Onboarding generoso — o oposto do paywall do concorrente. |
| **Assinatura** | Preço **justo** | Bandeira de confiança e transparência, não de "o mais barato". Valor real por preço honesto, sem reajuste-surpresa. |
| **Premium (Fase 2)** | IA & automação | Criativos com IA, contrato-IA assistido e lembrete automático — recursos que *custam* por uso pagam-se no plano de cima. |

> **Tensão registrada:** IA generativa **custa por uso** e não fecha com "ilimitado + barato". Por isso ela mora no plano premium, não no núcleo.

---

## 10. Roadmap por fases

**Fase 1 — MVP núcleo + Evento enxuto** `AGORA`
Agenda, Clientes, Catálogo, Financeiro, Evento (agrupamento + orçamento + sinal/saldo), orçamento enviável, lembrete `wa.me`.

**Fase 2 — Encantamento**
IA de criativo para redes sociais, contrato-IA assistido (template revisado por advogado), WhatsApp automático, séquito rico, deslocamento automático, Google/iOS calendar.

**Fase 3 — Expansão de persona**
Trazer a Bia (estúdio): recorrência, pacotes de sessões, controle de no-show. Depois, equipe/colaboradores.

---

## 11. Registro de decisões

| Status | Decisão |
|---|---|
| ✅ Decidido | Nicho: beleza (maquiagem, penteado, lash, nail, estética). Foco em **autônomo solo**. |
| ✅ Decidido | Beachhead: **Marina** (vai ao cliente). |
| ✅ Decidido | Bandeira de preço: **justo e transparente**, não "o mais barato". |
| ✅ Decidido | Modelo **híbrido** (agendamento átomo + Evento contêiner opcional) entra no MVP, na versão enxuta. |
| ✅ Decidido | Séquito na **opção leve** no MVP (lista de nomes). |
| ✅ Decidido | IA (criativo e contrato) fica na **Fase 2**. |
| ✅ Decidido | Lembrete WhatsApp **semiautomático** (grátis) no MVP; automático é premium. |
| ⏳ Em aberto | Confirmar catálogo unificado (recomendado) vs. duas entidades. |
| ⏳ Em aberto | Nome do produto (Áurea é codinome provisório). |
| ⏳ Em aberto | Faixa de preço da assinatura. |

---

## 12. Próximos passos

1. Confirmar o **catálogo unificado** (item único com atributos).
2. Desenhar os **fluxos de tela principais** (wireframe lógico): criar agendamento, criar Evento, montar orçamento, fechar financeiro.
3. Rodar este PRD com as **validadoras reais** (Marina & amigas) e coletar feedback.
4. Definir **nome** e **faixa de preço**.

---

*Documento vivo — evolui a cada conversa. Próxima atualização após a validação com as profissionais.*
