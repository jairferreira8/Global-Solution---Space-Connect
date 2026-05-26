# Prompt and Artificial Intelligence

> SolarGuard — Global Solution 2026.1 | FIAP 1CCPY

---

## 📌 Sobre esta entrega

Esta pasta contém o agente de IA da plataforma SolarGuard. Usando engenharia de prompt e um modelo de linguagem (LLM), o sistema interpreta os dados dos ciclos de monitoramento e gera análises inteligentes, previsões de falha e recomendações automáticas de ação em português.

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

## 🤖 O que o agente faz

Dado um ciclo de monitoramento com temperatura, comunicação, bateria, oxigênio e estabilidade, o agente:

- Analisa o **status atual** da missão
- **Prevê possíveis falhas** com base nas tendências dos dados
- Gera **recomendações automáticas** de ação
- Responde em linguagem natural em **português**

---

## 🧠 Engenharia de Prompt

O sistema utiliza prompts estruturados com:

- **Contexto do sistema**: define o papel do agente como controlador de missão
- **Dados de entrada**: os valores do ciclo atual em formato estruturado
- **Instruções de raciocínio**: orienta o modelo a analisar cada variável antes de concluir
- **Formato de saída**: exige resposta organizada em status, previsão e recomendação

---

## 📂 Arquivos

| Arquivo | Descrição |
|---|---|
| `agente_ia.py` | Código do agente com chamadas ao LLM e prompts documentados |
| `README.md` | Este arquivo |

---

## ▶️ Como executar

```bash
pip install requests
python agente_ia.py
```

---

## 💻 Repositório principal

[SolarGuard](../README.md)
