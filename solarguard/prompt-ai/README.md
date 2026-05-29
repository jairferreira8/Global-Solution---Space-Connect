# Prompt and Artificial Intelligence — Agente de IA

SolarGuard — Global Solution 2026.1 | FIAP 1CCPY

---

Agente de IA que interpreta os dados de cada ciclo de monitoramento do SolarGuard e gera análise de status, previsão e recomendação em linguagem natural. Usa o modelo Llama 3.1 via Groq API com engenharia de prompt (system prompt + user prompt com histórico de ciclos).

## Integrantes

| Nome | RM |
|---|---|
| Jair Ferreira dos Santos Neto | 569682 |
| Matheus da Costa Gonçalves | 570756 |
| Yan Luiz Neves Lemos | 571717 |

## Configuração da API Key

O arquivo `main.py` tem a variável `GROQ_API_KEY = "sua-API-aqui"` como placeholder. Para rodar, substitua pelo valor de uma chave real obtida em [console.groq.com](https://console.groq.com) (cadastro gratuito).

Não requer nenhuma biblioteca externa — usa apenas `urllib`, que já vem com o Python.

## Como executar

```bash
python main.py
```

---

[Voltar](../README.md)