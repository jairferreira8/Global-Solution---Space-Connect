import urllib.request
import json


GROQ_API_KEY = "sua-API-aqui"
GROQ_URL     = "https://api.groq.com/openai/v1/chat/completions"
MODELO = "llama-3.1-8b-instant"

# Parâmetros do modelo
TEMPERATURA  = 0.4   # Baixa = respostas mais objetivas e consistentes
MAX_TOKENS   = 600   # Suficiente para análise + recomendação detalhada
TOP_P        = 0.9   # Diversidade controlada nas respostas


RESET    = "\033[0m"
BOLD     = "\033[1m"
VERDE    = "\033[92m"
AMARELO  = "\033[93m"
VERMELHO = "\033[91m"
CIANO    = "\033[96m"
CINZA    = "\033[90m"
BRANCO   = "\033[97m"

# DADOS DA MISSÃO 

COLUNAS = ["temperatura", "comunicacao", "bateria", "oxigenio", "estabilidade"]

dados_missao = [
    [24, 95, 88, 97, 98],
    [27, 91, 80, 96, 94],
    [35, 72, 61, 94, 85],
    [48, 55, 38, 91, 70],
    [63, 30, 19, 88, 52],
    [45, 58, 35, 90, 67],
]

DESCRICOES_CICLO = [
    "Início da missão — sistemas nominais",
    "Estabilização — leve queda de bateria",
    "Queda parcial de comunicação e energia",
    "Alerta de energia — comunicação degradada",
    "Risco operacional elevado",
    "Tentativa de recuperação parcial",
]


# ENGENHARIA DE PROMPT

def montar_system_prompt():
    """
    Prompt de sistema: define o papel, o contexto e as regras
    de raciocínio do agente antes de receber qualquer dado.

    Boas práticas aplicadas:
    - Papel claro e específico (controlador de missão espacial)
    - Idioma forçado (português)
    - Instruções de raciocínio passo a passo (chain-of-thought)
    - Formato de saída definido explicitamente
    - Proibição de invenção de dados
    """
    return """Você é o Mission Control AI, o sistema de inteligência artificial da plataforma SolarGuard.

Sua função é analisar dados de ciclos de monitoramento de uma estação receptora de dados satelitais
e gerar análises precisas, previsões de falha e recomendações de ação.

CONTEXTO DO SISTEMA:
- A estação SolarGuard recebe dados de irradiância solar de satélites da NASA e ESA
- Os sensores monitoram 5 variáveis operacionais: temperatura, comunicação, bateria, oxigênio e estabilidade
- Cada ciclo representa um momento de coleta de dados

REGRAS DE RACIOCÍNIO (siga esta ordem antes de responder):
1. Analise cada variável individualmente e verifique se está dentro dos parâmetros normais
2. Identifique quais variáveis representam risco imediato
3. Verifique se existe combinação de variáveis que agrava o risco (ex: bateria baixa + comunicação falha)
4. Formule uma previsão baseada na tendência dos dados
5. Gere uma recomendação concreta e acionável

PARÂMETROS DE REFERÊNCIA:
- Temperatura: normal < 40°C | atenção 40–60°C | crítico > 60°C
- Comunicação: normal > 70% | atenção 40–70% | crítico < 40%
- Bateria: normal > 50% | atenção 20–50% | crítico < 20%
- Oxigênio: normal > 92% | atenção 85–92% | crítico < 85%
- Estabilidade: normal > 75% | atenção 55–75% | crítico < 55%

FORMATO DE RESPOSTA OBRIGATÓRIO (use exatamente estas seções):
📊 STATUS: [ESTÁVEL / ATENÇÃO / CRÍTICO] — justificativa em uma frase
⚠️ PREVISÃO: o que pode acontecer nos próximos ciclos se a tendência continuar
🛠️ RECOMENDAÇÃO: ação concreta e imediata que o operador deve tomar

RESTRIÇÕES:
- Responda sempre em português do Brasil
- Não invente dados que não foram fornecidos
- Seja direto e objetivo — sem introduções desnecessárias
- Máximo de 5 linhas por seção"""


def montar_user_prompt(numero_ciclo, dados_ciclo, descricao, historico):
    """
    Prompt de usuário: fornece os dados do ciclo atual e o
    histórico dos ciclos anteriores para contextualizar a análise.

    Boas práticas aplicadas:
    - Dados estruturados em formato legível pelo modelo
    - Contexto histórico para análise de tendência
    - Pergunta direta no final (task framing)
    """
    temp, comm, bat, ox, estab = dados_ciclo

    prompt = f"""CICLO ATUAL: {numero_ciclo} — {descricao}

DADOS DO CICLO {numero_ciclo}:
- Temperatura:   {temp}°C
- Comunicação:   {comm}%
- Bateria:       {bat}%
- Oxigênio:      {ox}%
- Estabilidade:  {estab}%
"""

    if historico:
        prompt += "\nHISTÓRICO DOS CICLOS ANTERIORES:\n"
        for h in historico:
            t, c, b, o, e = h["dados"]
            prompt += f"  Ciclo {h['numero']}: temp={t}°C | comm={c}% | bat={b}% | ox={o}% | estab={e}%\n"

    prompt += "\nAnalise os dados acima e responda no formato definido."
    return prompt



# CHAMADA À API 


def chamar_llm(system_prompt, user_prompt):
    """
    Realiza a chamada à API do Groq usando apenas urllib.
    Retorna o texto da resposta do modelo ou uma mensagem de erro.
    """
    payload = {
        "model": MODELO,
        "temperature": TEMPERATURA,
        "max_tokens": MAX_TOKENS,
        "top_p": TOP_P,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ]
    }

    dados = json.dumps(payload).encode("utf-8")

    requisicao = urllib.request.Request(
        url=GROQ_URL,
        data=dados,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(requisicao, timeout=30) as resposta:
            resultado = json.loads(resposta.read().decode("utf-8"))
            return resultado["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        codigo = e.code
        corpo = e.read().decode("utf-8")
        return f"❌ Erro HTTP {codigo}:\n{corpo}"
    except urllib.error.URLError:
        return "❌ Sem conexão com a internet. Verifique sua rede."
    except Exception as e:
        return f"❌ Erro inesperado: {str(e)}"


# EXIBIÇÃO

def linha(char="-", tamanho=60):
    print(CINZA + char * tamanho + RESET)


def exibir_cabecalho():
    print()
    linha("=")
    print(CIANO + BOLD + "  ☀  SOLARGUARD — AGENTE DE IA" + RESET)
    print(CINZA  + "  Análise Inteligente via Engenharia de Prompt" + RESET)
    print(CINZA  + "  Modelo: Llama 3 (Groq) | Global Solution 2026.1" + RESET)
    linha("=")
    print()


def exibir_ciclo(numero, descricao, dados, resposta_ia):
    temp, comm, bat, ox, estab = dados

    linha()
    print(f"{BOLD}  CICLO {numero} — {descricao}{RESET}")
    linha()
    print(f"  {CINZA}Temperatura: {temp}°C | Comunicação: {comm}% | Bateria: {bat}%{RESET}")
    print(f"  {CINZA}Oxigênio: {ox}%   | Estabilidade: {estab}%{RESET}")
    print()
    print(f"  {CIANO}{BOLD}Análise do Agente:{RESET}")
    print()

    for linha_texto in resposta_ia.strip().split("\n"):
        print(f"  {BRANCO}{linha_texto}{RESET}")

    print()


def exibir_rodape():
    linha("=")
    print(CINZA + "  SolarGuard Mission Control AI — FIAP 2026" + RESET)
    linha("=")
    print()


# EXECUÇÃO PRINCIPAL

def main():
    exibir_cabecalho()

    if GROQ_API_KEY == "sua-chave-aqui":
        print(f"{VERMELHO}{BOLD}  ATENÇÃO: Chave de API não configurada.{RESET}")
        print(f"  Acesse {CIANO}https://console.groq.com{RESET} e insira sua chave")
        print(f"  na variável {AMARELO}GROQ_API_KEY{RESET} no início do arquivo.")
        print()
        return

    system_prompt = montar_system_prompt()
    historico = []

    for i, ciclo in enumerate(dados_missao):
        numero = i + 1
        descricao = DESCRICOES_CICLO[i]

        print(f"  {CINZA}Consultando o agente para o ciclo {numero}...{RESET}")

        user_prompt = montar_user_prompt(numero, ciclo, descricao, historico)
        resposta = chamar_llm(system_prompt, user_prompt)

        exibir_ciclo(numero, descricao, ciclo, resposta)

        historico.append({"numero": numero, "dados": ciclo})

    exibir_rodape()


if __name__ == "__main__":
    main()