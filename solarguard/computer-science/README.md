# Computer Science — Lógica Digital de Alertas

SolarGuard — Global Solution 2026.1 | FIAP 1CCPY

---

Sistema de alertas por lógica booleana aplicado aos ciclos de monitoramento do SolarGuard. Define 5 variáveis de entrada a partir das condições operacionais do módulo orbital e avalia uma expressão lógica que aciona o alerta (X = 1) quando há risco à operação.

## Variáveis

| Var | Condição |
|---|---|
| A | Comunicação < 30% |
| B | Temperatura > 35°C |
| C | Bateria < 20% |
| D | Estabilidade < 40% |
| E | Oxigênio < 80% |

## Expressão

```
X = (A AND B) OR C OR (D AND E)
```

O código gera a tabela verdade completa (32 combinações) e avalia os 6 ciclos da missão.

## Integrantes

| Nome | RM |
|---|---|
| Jair Ferreira dos Santos Neto | 569682 |
| Matheus da Costa Gonçalves | 570756 |
| Yan Luiz Neves Lemos | 571717 |

## Como executar

```bash
python logica_booleana.py
```

---

[Voltar](../README.md)
