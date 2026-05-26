# Modelagem Matemática e Computacional

> SolarGuard — Global Solution 2026.1 | FIAP 1CCPY

---

## 📌 Sobre esta entrega

Esta pasta contém os modelos matemáticos desenvolvidos para o contexto espacial do projeto SolarGuard. Os modelos traduzem fenômenos físicos reais para linguagem matemática, respeitando o comportamento físico esperado.

---

## 👥 Integrantes

| Nome | RM |
|---|---|
| Jair Ferreira dos Santos Neto | 569682 |
| Matheus da Costa Gonçalves | 570756 |
| Yan Luiz Neves Lemos | 571717 |
| Arthur dos Santos Bezerra | 569721 |
| Carlos Henrique Fratezi | 571792 |

---

## 📐 Modelos Desenvolvidos

### Modelo 1 — P(t): Pressão Aerodinâmica durante o Lançamento

Representa o comportamento da pressão aerodinâmica sobre o satélite durante a fase de subida. A função deve:
- Começar em zero no instante t = 0
- Crescer rapidamente nas camadas mais densas da atmosfera
- Atingir um ponto de máximo (Max Q)
- Decair após a saída das camadas densas

**Família de funções:** polinomial de 2º grau (parábola com abertura para baixo)

---

### Modelo 2 — R(T): Risco de Falha em Função da Temperatura

Representa o risco de falha dos componentes eletrônicos do satélite em função da temperatura. Inspirado no acidente Challenger, a função deve:
- Crescer quando a temperatura cai (risco alto no frio)
- Decair quando a temperatura sobe (risco menor no calor)
- Nunca atingir zero — existe sempre um risco residual mínimo (assíntota horizontal)

**Família de funções:** exponencial decrescente com assíntota horizontal

---

## 📂 Arquivos

| Arquivo | Descrição |
|---|---|
| `modelos.pdf` | Relatório com funções, gráficos, domínio, derivadas e análise de máximos/mínimos |
| `README.md` | Este arquivo |

---

## 💻 Repositório principal

[SolarGuard](../README.md)
