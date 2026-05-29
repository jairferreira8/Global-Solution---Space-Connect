# ☀️ SolarGuard — Plataforma de Inteligência Solar via Dados Satelitais

> Global Solution 2026.1 — FIAP | Turma 1CCPY | Space Connect

---

## 📌 Sobre o Projeto

O **SolarGuard** é uma plataforma de inteligência energética que consome dados de irradiância solar já coletados por satélites públicos — como o **NASA POWER**, o **Copernicus (ESA)** e o **INPE** — e os transforma em informação acionável para quem opera painéis solares e eletropostos no Brasil.

O satélite não é construído por nós. Ele já existe e já coleta esses dados gratuitamente. O que construímos é a camada que transforma esses dados em inteligência: um pipeline de processamento, modelos matemáticos, lógica de alertas, análise estatística e um agente de IA que interpreta tudo e gera recomendações em linguagem natural.

---

## 🚀 Conexão com o Tema Space Connect

A tecnologia espacial — especificamente o **sensoriamento remoto por satélite** — é o insumo principal da plataforma. Dados que satélites da NASA e ESA coletam em órbita são o ponto de partida de toda a inteligência gerada pelo sistema. Sem os dados orbitais, a solução não existe.

---

## 👥 Grupo 5

| Nome | RM |
|---|---|
| Jair Ferreira dos Santos Neto | 569682 |
| Matheus da Costa Gonçalves | 570756 |
| Yan Luiz Neves Lemos | 571717 |

---

## 🗂️ Estrutura do Repositório

Cada pasta corresponde à entrega de uma disciplina. O projeto é **um sistema único** — as partes se complementam e constroem a mesma plataforma.

```
solarguard/
├── pensamento-computacional/   → Mission Control AI (núcleo do sistema)
├── data-structures/            → Pipeline de dados e menu interativo
├── computer-science/           → Lógica booleana de alertas
├── prompt-ai/                  → Agente de IA com LLM
├── energias-renovaveis/        → Monitoramento do subsistema energético
├── modelagem-linear/           → Análise estatística do dataset satelital
├── modelagem-matematica/       → Modelos P(t) e R(T)
└── coa/                        → Simulação IoT no Wokwi
```

---

## 🧱 Arquitetura da Plataforma

```
[ Satélites NASA / ESA / INPE ]
           │
           ▼
  [ API de Dados Satelitais ]
           │
           ▼
  [ Pipeline de Dados ]  ←── Data Structures
           │
           ▼
  [ dados_missao matrix ]  ←── Pensamento Computacional
     temperatura | comunicacao | bateria | oxigenio | estabilidade
           │
     ┌─────┴──────────────────────┐
     ▼                            ▼
[ Lógica Booleana ]         [ Agente de IA ]
   Computer Science           Prompt & AI
     │                            │
     └──────────┬─────────────────┘
                ▼
     [ Relatório / Alertas / Recomendações ]
```

---

## 📡 Fontes de Dados

| Fonte | Dados | Link |
|---|---|---|
| NASA POWER API | Irradiância solar por coordenada geográfica | https://power.larc.nasa.gov |
| Copernicus / ESA | Cobertura de nuvens, radiação solar | https://www.copernicus.eu |
| INPE / SONDA | Atlas solarimétrico brasileiro | https://sonda.ccst.inpe.br |
| Kaggle | Datasets de telemetria satelital | https://www.kaggle.com |

---

## 🎯 ODS Alinhados

- **ODS 7** — Energia limpa e acessível
- **ODS 9** — Indústria, inovação e infraestrutura
- **ODS 11** — Cidades e comunidades sustentáveis
- **ODS 13** — Ação contra a mudança global do clima

---

## 📁 Navegue pelas Disciplinas

- [Pensamento Computacional](./pensamento-computacional/README.md)
- [Data Structures and Algorithms](./data-structures/README.md)
- [Computer Science](./computer-science/README.md)
- [Prompt and Artificial Intelligence](./prompt-ai/README.md)
- [Soluções em Energias Renováveis](./energias-renovaveis/README.md)
- [Modelagem Linear para Aprendizado de Máquina](./modelagem-linear/README.md)
- [Modelagem Matemática e Computacional](./modelagem-matematica/README.md)
- [Computer Organization and Architecture](./coa/README.md)
