# Modelagem Linear — Análise Estatística de Irradiância Solar

SolarGuard — Global Solution 2026.1 | FIAP 1CCPY

---

Análise estatística descritiva da irradiância solar diária em São Paulo ao longo de 2023, com base em dados reais da NASA POWER API (365 registros). Inclui distribuição de frequências para variável discreta (mês) e contínua (irradiância em classes pela Regra de Sturges), análise univariada completa e relatório com interpretação dos resultados.

## Integrantes

| Nome | RM |
|---|---|
| Jair Ferreira dos Santos Neto | 569682 |
| Matheus da Costa Gonçalves | 570756 |
| Yan Luiz Neves Lemos | 571717 |

## Como executar

Rode a partir da pasta `modelagem-linear/`:

```bash
pip install pandas matplotlib scipy
python analise.py
```

Gera dois gráficos (`grafico1_irradiancia_mensal.png` e `grafico2_histograma_irradiancia.png`) usados no relatório.

## Fonte dos dados

NASA POWER API — São Paulo, SP (lat: −23,55 / lon: −46,63) | 2023

---

[Voltar](../README.md)
