# Prompt and Artificial Intelligence

> SolarGuard — Global Solution 2026.1 | FIAP 1CCPY

---

## 📌 Sobre esta entrega

Esta pasta contém o agente de IA da plataforma SolarGuard. Usando engenharia de prompt e o modelo Llama 3, o sistema interpreta os dados dos ciclos de monitoramento e gera análises inteligentes, previsões de falha e recomendações automáticas de ação em português.

---

## 👥 Integrantes

| Nome | RM |
|---|---|
| Jair Ferreira dos Santos Neto | 569682 |
| Yan Luiz Neves Lemos | 571717 |
| Matheus da Costa Gonçalves | 570756 |

---

## ⚙️ Pré-requisitos

### Opção 1 — Groq API (recomendado, online)

1. Acesse [https://console.groq.com](https://console.groq.com) e crie uma conta gratuita
2. No menu lateral, clique em **API Keys → Create API Key**
3. Copie a chave gerada (começa com `gsk_...`)
4. No arquivo `main.py`, substitua:
```python
   GROQ_API_KEY = "sua-chave-aqui"
```
   pela sua chave real

Não é necessário instalar nenhuma biblioteca — o código usa apenas `urllib`, que já vem com o Python.

---

### Opção 2 — Ollama (offline, local)

Caso prefira rodar o modelo localmente sem depender de internet:

1. Acesse [https://ollama.com](https://ollama.com) e baixe o instalador para o seu sistema
2. Instale o Ollama normalmente
3. Abra o terminal e execute:
```bash
   ollama pull llama3
```
4. Para iniciar o servidor local:
```bash
   ollama serve
```

> ⚠️ O código atual está configurado para a Groq API. Para usar o Ollama, é necessário alterar a URL e o formato da requisição no arquivo `main.py`.

---

## ▶️ Como executar

```bash
python main.py
```

---

## 📂 Arquivos

| Arquivo | Descrição |
|---|---|
| `main.py` | Agente de IA com chamadas ao LLM e prompts documentados |
| `README.md` | Este arquivo |

