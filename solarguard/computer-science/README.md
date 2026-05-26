# Computer Science — Mission Control AI: Lógica Digital de Alertas

> SolarGuard — Global Solution 2026.1 | FIAP 1CCPY

---

## 📌 Sobre esta entrega

Esta pasta contém o sistema de alertas por lógica digital da plataforma SolarGuard. A partir das variáveis operacionais dos ciclos de monitoramento, foram definidas expressões booleanas que acionam o alerta principal do sistema (X = 1) sempre que condições críticas forem detectadas.

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

## 🔣 Variáveis de Entrada

| Variável | Condição | Valor 1 (risco) |
|---|---|---|
| A | Falha de comunicação | Comunicação = 0 |
| B | Temperatura crítica | Temperatura > 80°C |
| C | Energia baixa | Bateria < 20% |
| D | Instabilidade operacional | Estabilidade < limiar |
| E | Nível de oxigênio crítico | Oxigênio < limiar |

---

## ⚡ Expressão Lógica

```
X = (A AND C) OR (B AND D) OR (E AND NOT C)
```

- Se houver falha de comunicação **E** energia baixa → alerta
- Se temperatura crítica **E** instabilidade → alerta
- Se oxigênio crítico **E** energia não estiver baixa → alerta

---

## 📂 Arquivos

| Arquivo | Descrição |
|---|---|
| `logica_booleana.md` | Expressão lógica, tabela verdade e diagrama de portas |
| `README.md` | Este arquivo |

---

## 💻 Repositório principal

[SolarGuard](../README.md)
