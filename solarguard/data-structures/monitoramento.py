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

historico = []
ciclo_atual = [0]


def limpar():
    print("\033[2J\033[H", end="")


def linha(char="─", tam=60, cor=CINZA):
    print(cor + char * tam + RESET)


def pausar():
    print()
    input(CINZA + "  Pressione ENTER para continuar..." + RESET)


def barra(valor, tam=20):
    preenchido = int((valor / 100) * tam)
    vazio = tam - preenchido
    cor = VERDE if valor >= 60 else (AMARELO if valor >= 30 else VERMELHO)
    return cor + "█" * preenchido + CINZA + "░" * vazio + RESET + f" {valor:.0f}%"


def verificar_alertas(dado):
    temp, comm, bat, ox, estab = dado
    alertas = []

    if temp > 80:
        alertas.append((VERMELHO, "SUPERAQUECIMENTO", f"Temperatura crítica: {temp}°C > 80°C"))
    elif temp > 40:
        alertas.append((AMARELO, "TEMP. ELEVADA", f"Temperatura em atenção: {temp}°C"))

    if comm == 0:
        alertas.append((VERMELHO, "FALHA DE COMUNICAÇÃO", "Sinal completamente perdido"))
    elif comm < 50:
        alertas.append((AMARELO, "COMUNICAÇÃO FRACA", f"Sinal degradado: {comm}%"))

    if bat < 20:
        alertas.append((VERMELHO, "BATERIA CRÍTICA", f"Modo economia ativado — {bat}%"))
    elif bat < 50:
        alertas.append((AMARELO, "BATERIA BAIXA", f"Nível de atenção: {bat}%"))

    if ox < 80:
        alertas.append((VERMELHO, "OXIGÊNIO CRÍTICO", f"Nível perigoso: {ox}%"))
    elif ox < 90:
        alertas.append((AMARELO, "OXIGÊNIO BAIXO", f"Monitorar: {ox}%"))

    if estab < 40:
        alertas.append((VERMELHO, "INSTABILIDADE CRÍTICA", f"Estabilidade em {estab}%"))
    elif estab < 70:
        alertas.append((AMARELO, "INSTABILIDADE", f"Estabilidade reduzida: {estab}%"))

    return alertas


def simular_ciclo():
    linha("═", 60, AZUL)
    print(AZUL + BOLD + "  SIMULAR CICLO DE MONITORAMENTO" + RESET)
    linha("═", 60, AZUL)
    print()

    idx = ciclo_atual[0]
    if idx >= len(dados_missao):
        print(f"  {AMARELO}Todos os {len(dados_missao)} ciclos já foram simulados.{RESET}")
        pausar()
        return

    dado = dados_missao[idx]
    temp, comm, bat, ox, estab = dado
    desc = DESCRICOES_CICLO[idx]
    ciclo_atual[0] += 1

    print(f"  {CINZA}Lendo sensores...{RESET}")
    time.sleep(0.5)
    print(f"  {CINZA}Processando ciclo {ciclo_atual[0]}...{RESET}")
    time.sleep(0.4)
    print()

    cor_t = VERDE if temp <= 30 else (AMARELO if temp <= 35 else VERMELHO)

    linha("─", 60, AZUL)
    print(f"  {BOLD}CICLO {ciclo_atual[0]:02d}{RESET}  —  {CINZA}{desc}{RESET}")
    linha("─", 60, AZUL)
    print(f"  {'Temperatura':<16} {cor_t}{temp}°C{RESET}")
    print(f"  {'Comunicação':<16} {barra(comm)}")
    print(f"  {'Bateria':<16} {barra(bat)}")
    print(f"  {'Oxigênio':<16} {barra(ox)}")
    print(f"  {'Estabilidade':<16} {barra(estab)}")
    linha("─", 60, AZUL)

    alertas = verificar_alertas(dado)
    if alertas:
        print(f"\n  {BOLD}Alertas detectados:{RESET}")
        for cor, tag, msg in alertas:
            print(f"  {cor}{BOLD}[{tag}]{RESET} {msg}")
    else:
        print(f"\n  {VERDE}Nenhum alerta — ciclo dentro dos parâmetros normais.{RESET}")

    historico.append((ciclo_atual[0], dado, desc))
    print(f"\n  {CINZA}Ciclo registrado no histórico.{RESET}")
    pausar()


def ver_status():
    linha("═", 60, CIANO)
    print(CIANO + BOLD + "  STATUS ATUAL DA MISSÃO" + RESET)
    linha("═", 60, CIANO)
    print()

    if not historico:
        print(f"  {CINZA}Nenhum ciclo simulado ainda. Use a opção 1 primeiro.{RESET}")
        pausar()
        return

    num, dado, desc = historico[-1]
    temp, comm, bat, ox, estab = dado
    cor_t = VERDE if temp <= 30 else (AMARELO if temp <= 35 else VERMELHO)

    print(f"  {BOLD}Último ciclo:{RESET} {CIANO}Ciclo {num:02d}{RESET}  —  {CINZA}{desc}{RESET}")
    print()
    print(f"  {'Temperatura':<16} {cor_t}{temp}°C{RESET}")
    print(f"  {'Comunicação':<16} {barra(comm)}")
    print(f"  {'Bateria':<16} {barra(bat)}")
    print(f"  {'Oxigênio':<16} {barra(ox)}")
    print(f"  {'Estabilidade':<16} {barra(estab)}")
    print()

    alertas = verificar_alertas(dado)
    if alertas:
        linha("─", 60, VERMELHO)
        print(f"  {VERMELHO}{BOLD}SISTEMA COM ALERTAS ATIVOS{RESET}")
        linha("─", 60, VERMELHO)
        for cor, tag, msg in alertas:
            print(f"  {cor}▶ [{tag}] {msg}{RESET}")
    else:
        linha("─", 60, VERDE)
        print(f"  {VERDE}{BOLD}SISTEMA OPERACIONAL — SEM ALERTAS{RESET}")
        linha("─", 60, VERDE)

    pausar()


def executar_analise():
    linha("═", 60, MAGENTA)
    print(MAGENTA + BOLD + "  ANÁLISE DOS CICLOS MONITORADOS" + RESET)
    linha("═", 60, MAGENTA)
    print()

    if not historico:
        print(f"  {CINZA}Nenhum ciclo no histórico ainda.{RESET}")
        pausar()
        return

    dados = [d for _, d, _ in historico]
    n = len(dados)

    print(f"  {BOLD}Ciclos analisados: {CIANO}{n}{RESET}")
    print()

    rotulos = ["Temperatura", "Comunicação", "Bateria", "Oxigênio", "Estabilidade"]
    cabecalho = f"  {'Variável':<16} {'Mín':>6} {'Máx':>6} {'Média':>8}"
    print(BOLD + cabecalho + RESET)
    linha("─", 60, CINZA)

    for col, rot in enumerate(rotulos):
        vals = [d[col] for d in dados]
        mn, mx, med = min(vals), max(vals), sum(vals) / n
        cor = VERDE if med >= 60 else (AMARELO if med >= 30 else VERMELHO)
        print(f"  {rot:<16} {mn:>6.0f} {mx:>6.0f}  {cor}{med:>7.1f}{RESET}")

    criticos = sum(1 for _, d, _ in historico if verificar_alertas(d))
    pct = (criticos / n) * 100
    cor = VERDE if pct < 30 else (AMARELO if pct < 60 else VERMELHO)
    print(f"\n  Ciclos com alertas: {cor}{criticos}/{n} ({pct:.0f}%){RESET}")

    if n >= 2:
        delta_bat = dados[-1][2] - dados[0][2]
        if delta_bat > 0:
            print(f"  Tendência da bateria: {VERDE}▲ Recuperando (+{delta_bat:.0f}%){RESET}")
        elif delta_bat < 0:
            print(f"  Tendência da bateria: {VERMELHO}▼ Drenando ({delta_bat:.0f}%){RESET}")
        else:
            print(f"  Tendência da bateria: {CINZA}► Estável{RESET}")

    pausar()


def ver_historico():
    linha("═", 60, AMARELO)
    print(AMARELO + BOLD + "  HISTÓRICO DE LEITURAS" + RESET)
    linha("═", 60, AMARELO)
    print()

    if not historico:
        print(f"  {CINZA}Nenhum ciclo registrado ainda.{RESET}")
        pausar()
        return

    cabecalho = f"  {'Ciclo':>5}  {'Temp':>5}  {'Comm':>5}  {'Bat':>5}  {'O₂':>5}  {'Estab':>6}  Status"
    print(BOLD + cabecalho + RESET)
    linha("─", 60, CINZA)

    for num, dado, _ in historico:
        temp, comm, bat, ox, estab = dado
        tem_alerta = verificar_alertas(dado)
        status = VERDE + "OK     " + RESET if not tem_alerta else VERMELHO + "ALERTA " + RESET
        cor_t = VERDE if temp <= 30 else (AMARELO if temp <= 35 else VERMELHO)
        cor_b = VERDE if bat >= 50 else (AMARELO if bat >= 20 else VERMELHO)
        print(
            f"  {CIANO}{num:>5}{RESET}  "
            f"{cor_t}{temp:>4}°{RESET}  "
            f"{comm:>4}%  "
            f"{cor_b}{bat:>4}%{RESET}  "
            f"{ox:>4}%  "
            f"{estab:>5}%  "
            f"{status}"
        )

    print()
    print(f"  {CINZA}Total de registros: {len(historico)}{RESET}")
    pausar()


def cabecalho_menu():
    limpar()
    print()
    linha("═", 60, CIANO)
    print(CIANO + BOLD + "  ☀  SOLARGUARD — Sistema de Monitoramento" + RESET)
    print(CINZA  + "  Data Structures and Algorithms | Global Solution 2026.1" + RESET)
    linha("═", 60, CIANO)
    restantes = len(dados_missao) - ciclo_atual[0]
    print(
        f"\n  {CINZA}Ciclos disponíveis: {BRANCO}{restantes}{CINZA}  |  "
        f"Histórico: {BRANCO}{len(historico)} registro(s){RESET}\n"
    )


def menu():
    while True:
        cabecalho_menu()

        opcoes = [
            (AZUL,    "1", "Inserir dados — simular próximo ciclo"),
            (CIANO,   "2", "Visualizar status atual da missão"),
            (MAGENTA, "3", "Executar análise dos ciclos"),
            (AMARELO, "4", "Histórico das leituras"),
            (CINZA,   "5", "Encerrar sistema"),
        ]

        for cor, num, desc in opcoes:
            print(f"  {cor}{BOLD}[{num}]{RESET}  {desc}")

        print()
        linha("─", 60, CINZA)
        escolha = input(f"  {BRANCO}Opção: {RESET}").strip()

        if escolha == "1":
            simular_ciclo()
        elif escolha == "2":
            ver_status()
        elif escolha == "3":
            executar_analise()
        elif escolha == "4":
            ver_historico()
        elif escolha == "5":
            limpar()
            print()
            linha("═", 60, CINZA)
            print(CINZA + BOLD + "  SolarGuard encerrado." + RESET)
            linha("═", 60, CINZA)
            print()
            break
        else:
            print(f"\n  {VERMELHO}Opção inválida. Digite um número de 1 a 5.{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    menu()
