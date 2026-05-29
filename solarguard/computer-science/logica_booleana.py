import time

RESET    = "\033[0m"
BOLD     = "\033[1m"
VERDE    = "\033[92m"
AMARELO  = "\033[93m"
VERMELHO = "\033[91m"
CIANO    = "\033[96m"
AZUL     = "\033[94m"
MAGENTA  = "\033[95m"
CINZA    = "\033[90m"
BRANCO   = "\033[97m"

# ── Dados da missão ────────────────────────────────────────────
# [temperatura(°C), comunicacao(%), bateria(%), oxigenio(%), estabilidade(%)]
dados_missao = [
    [22, 98, 87, 95, 90],
    [31, 94, 76, 93, 85],
    [45, 87, 61, 90, 70],
    [58, 72, 42, 85, 55],
    [38, 89, 55, 92, 75],
    [27, 96, 71, 94, 82],
]

DESCRICOES_CICLO = [
    "Conexão inicial com satélite NASA POWER",
    "Estabilização da janela de coleta",
    "Interferência atmosférica detectada",
    "Degradação do canal de comunicação",
    "Tentativa de realinhamento do link satelital",
    "Restabelecimento do link e normalização",
]

# ── Variáveis de entrada ───────────────────────────────────────
#
#  A — Falha de comunicação com o módulo orbital  (comunicacao < 30%)
#  B — Temperatura crítica do módulo receptor     (temperatura > 35°C)
#  C — Nível crítico de energia / bateria         (bateria < 20%)
#  D — Instabilidade operacional da estação       (estabilidade < 40%)
#  E — Nível crítico de oxigênio no módulo        (oxigenio < 80%)
#
# ── Expressão lógica ──────────────────────────────────────────
#
#  X = (A AND B) OR C OR (D AND E)
#
#  Regras:
#  • Falha de comunicação  E  temperatura crítica  → alerta (módulo em risco de perda total)
#  • Bateria crítica sozinha                       → alerta (operação comprometida)
#  • Instabilidade E oxigênio crítico              → alerta (módulo em condição de perigo)


def linha(char="─", tam=64, cor=CINZA):
    print(cor + char * tam + RESET)


def extrair_variaveis(dado):
    temp, comm, bat, ox, estab = dado
    A = 1 if comm  < 30  else 0
    B = 1 if temp  > 35  else 0
    C = 1 if bat   < 20  else 0
    D = 1 if estab < 40  else 0
    E = 1 if ox    < 80  else 0
    return A, B, C, D, E


def avaliar_expressao(A, B, C, D, E):
    return int((A and B) or C or (D and E))


def exibir_cabecalho():
    print()
    linha("═", 64, CIANO)
    print(CIANO + BOLD + "  ☀  SOLARGUARD — Lógica Digital de Alertas" + RESET)
    print(CINZA  + "  Computer Science | Global Solution 2026.1" + RESET)
    linha("═", 64, CIANO)
    print()
    time.sleep(0.4)


def exibir_variaveis():
    print(f"  {BOLD}Variáveis de entrada:{RESET}\n")
    variaveis = [
        ("A", "Falha de comunicação com o módulo orbital", "comunicação < 30%"),
        ("B", "Temperatura crítica do módulo receptor",    "temperatura > 35°C"),
        ("C", "Nível crítico de energia",                  "bateria < 20%"),
        ("D", "Instabilidade operacional da estação",      "estabilidade < 40%"),
        ("E", "Nível crítico de oxigênio no módulo",       "oxigênio < 80%"),
    ]
    for var, desc, cond in variaveis:
        print(f"  {CIANO}{BOLD}{var}{RESET}  {CINZA}({cond}){RESET}")
        print(f"     {desc}")
        print()


def exibir_expressao():
    linha("─", 64, AZUL)
    print(f"  {BOLD}Expressão lógica:{RESET}\n")
    print(f"  {AMARELO}{BOLD}  X  =  (A  AND  B)  OR  C  OR  (D  AND  E){RESET}\n")
    print(f"  {CINZA}Portas utilizadas: AND · OR · NOT (implícito nas condições){RESET}")
    print()
    print(f"  {CINZA}Regras:{RESET}")
    print(f"  {CINZA}  • Falha de comunicação E temperatura crítica  →  risco de perda do módulo{RESET}")
    print(f"  {CINZA}  • Bateria crítica isolada                     →  operação comprometida{RESET}")
    print(f"  {CINZA}  • Instabilidade E oxigênio crítico            →  módulo em condição de perigo{RESET}")
    linha("─", 64, AZUL)
    print()


def exibir_tabela_verdade():
    print(f"  {BOLD}Tabela verdade completa  {CINZA}(32 combinações — 5 variáveis){RESET}\n")

    cab = f"  {'A':>3} {'B':>3} {'C':>3} {'D':>3} {'E':>3}   {'X':>3}   Situação"
    print(BOLD + cab + RESET)
    linha("─", 64, CINZA)

    for i in range(32):
        A = (i >> 4) & 1
        B = (i >> 3) & 1
        C = (i >> 2) & 1
        D = (i >> 1) & 1
        E = (i >> 0) & 1
        X = avaliar_expressao(A, B, C, D, E)

        cor_x = VERMELHO if X else VERDE
        situacao = f"{VERMELHO}ALERTA ACIONADO{RESET}" if X else f"{VERDE}operação normal{RESET}"

        def b(v):
            return (VERMELHO if v else CINZA) + str(v) + RESET

        print(f"  {b(A):>3} {b(B):>3} {b(C):>3} {b(D):>3} {b(E):>3}   {cor_x}{BOLD}{X}{RESET}   {situacao}")

    print()


def exibir_avaliacao_ciclos():
    linha("═", 64, MAGENTA)
    print(MAGENTA + BOLD + "  AVALIAÇÃO DOS CICLOS DA MISSÃO" + RESET)
    linha("═", 64, MAGENTA)
    print()

    alertas_acionados = 0

    for i, dado in enumerate(dados_missao):
        A, B, C, D, E = extrair_variaveis(dado)
        X = avaliar_expressao(A, B, C, D, E)
        temp, comm, bat, ox, estab = dado
        desc = DESCRICOES_CICLO[i]

        cor_x = VERMELHO if X else VERDE
        status = f"{VERMELHO}{BOLD}ALERTA  X=1{RESET}" if X else f"{VERDE}Normal  X=0{RESET}"

        linha("─", 64, AZUL)
        print(f"  {BOLD}CICLO {i+1}{RESET}  —  {CINZA}{desc}{RESET}")
        linha("─", 64, AZUL)

        def bit(v, label):
            cor = VERMELHO if v else CINZA
            return f"{cor}{BOLD}{label}={v}{RESET}"

        print(f"  {bit(A,'A')}  {bit(B,'B')}  {bit(C,'C')}  {bit(D,'D')}  {bit(E,'E')}")
        print(f"  {CINZA}temp={temp}°C  comm={comm}%  bat={bat}%  ox={ox}%  estab={estab}%{RESET}")
        print()
        print(f"  X = (A·B) + C + (D·E)  =  ({A}·{B}) + {C} + ({D}·{E})  =  {cor_x}{BOLD}{X}{RESET}")
        print(f"  Resultado: {status}")
        print()

        if X:
            alertas_acionados += 1
            motivos = []
            if A and B:
                motivos.append("falha de comunicação + temperatura crítica")
            if C:
                motivos.append("bateria crítica")
            if D and E:
                motivos.append("instabilidade + oxigênio crítico")
            print(f"  {VERMELHO}Causa: {', '.join(motivos)}{RESET}")
            print()

        time.sleep(0.15)

    linha("═", 64, MAGENTA)
    print(f"\n  {BOLD}Ciclos com alerta acionado:{RESET}  "
          f"{VERMELHO if alertas_acionados else VERDE}{alertas_acionados}/{len(dados_missao)}{RESET}")
    pct = (alertas_acionados / len(dados_missao)) * 100
    cor = VERDE if pct == 0 else (AMARELO if pct < 50 else VERMELHO)
    print(f"  {BOLD}Taxa de alerta:{RESET}              {cor}{pct:.0f}%{RESET}")
    linha("═", 64, MAGENTA)
    print()


def main():
    exibir_cabecalho()
    exibir_variaveis()
    exibir_expressao()
    exibir_tabela_verdade()
    exibir_avaliacao_ciclos()


if __name__ == "__main__":
    main()
