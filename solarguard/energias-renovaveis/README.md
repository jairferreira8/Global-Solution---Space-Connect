# 🛸 SolarGuard

Esse projeto nasceu de uma pergunta simples: e se a gente pudesse monitorar o subsistema de energia solar de uma missão espacial em tempo real, receber alertas automáticos quando algo está errado e ainda ter o sistema sugerindo o que fazer?

Foi isso que a gente tentou construir com o SolarGuard.

---

## A ideia

A missão espacial gera dados a cada ciclo — irradiância solar captada pelos painéis, consumo dos módulos, temperatura e nível de bateria. O SolarGuard lê esses dados, analisa ciclo por ciclo e toma decisões automáticas com base no que está acontecendo.

Se a irradiância cair demais, o sistema avisa. Se o consumo ultrapassar a geração, o sistema avisa. Se a bateria chegar numa situação crítica, o sistema aciona o backup sozinho. No final, ainda plota um gráfico mostrando toda a curva de carga da missão.

A inspiração para os dados de irradiância vem de satélites reais — NASA POWER, Copernicus e INPE já coletam esses dados gratuitamente. A gente pega essa ideia e aplica no contexto da missão espacial simulada.

---

## O que o sistema faz

- Lê os dados simulados de 10 ciclos de monitoramento da missão
- Calcula a geração solar estimada com base na irradiância captada
- Compara geração vs consumo e detecta déficit energético
- Dispara alertas automáticos quando algo está fora do normal
- Decide automaticamente uma ação: modo econômico, carga de bateria ou acionamento de backup
- Gera um gráfico com a curva de carga e o nível de bateria ao longo de todos os ciclos

---

## Como rodar

Você vai precisar do Python 3 instalado. Depois é só instalar o matplotlib:

```bash
pip install matplotlib
```

E rodar:

```bash
python solarguard.py
```

O terminal vai mostrar o relatório ciclo a ciclo, e no final abre o gráfico automaticamente.

---

## Exemplo do que aparece no terminal

```
=================================================================
   🛸 SOLARGUARD — Monitoramento Energético Solar
   Missão Espacial Experimental | Grupo 5 — 1CCPY FIAP
=================================================================

📡 CICLO 06
   Irradiância : 90 W/m²
   Geração     : 32.4 W
   Consumo     : 720 W
   Temperatura : 41°C
   Bateria     : 35%
   ⚠️  Irradiância baixa (90 W/m²) — geração comprometida
   🔴 CRÍTICO: Bateria em 35% — abaixo do limite seguro
   🌡️  Temperatura crítica nos painéis (41°C)
   🚨 AÇÃO: Acionar fonte de backup — bateria crítica e geração insuficiente
```

---

## Estrutura dos arquivos

```
SolarGuard/
│
├── solarguard.py              # o código principal
├── solarguard_curva_carga.png # gráfico gerado ao rodar o código
└── README.md                  # você está aqui
```

---

## Por que isso importa

O Brasil tem um dos maiores potenciais solares do mundo, mas boa parte disso é desperdiçada porque quem opera sistemas fotovoltaicos não tem visibilidade de geração futura. Saber com antecedência que a irradiância vai cair permite tomar decisões melhores: carregar bateria antes, redistribuir carga, ou acionar backup no momento certo.

Esse projeto se alinha com três ODS da ONU:

- **ODS 7** — Energia Limpa e Acessível
- **ODS 9** — Indústria, Inovação e Infraestrutura
- **ODS 13** — Ação Contra a Mudança Global do Clima

---

## Quem fez

| Nome | RM |
|------|----|
| Matheus da Costa Gonçalves | 570756 |
| Jair Ferreira dos Santos Neto | 569682 |
| Yan Luiz Neves Lemos | 571717 |

Turma 1CCPY — FIAP
Global Solution 2026.1 — Soluções em Energias Renováveis e Sustentáveis

---

## Vídeo

🔗 [Assistir no YouTube](#) *(link será adicionado após a gravação)*
