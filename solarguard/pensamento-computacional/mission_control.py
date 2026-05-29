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

NOME_MISSAO = "SolarGuard Alpha"
NOME_EQUIPE = "Grupo 5 — 1CCPY"

# [temperatura(°C), comunicacao(%), bateria(%), oxigenio(%), estabilidade(%)]
dados_missao = [
    [22, 98, 87, 95, 90],
    [31, 94, 76, 93, 85],
    [45, 87, 61, 90, 70],
    [58, 72, 42, 85, 55],
    [38, 89, 55, 92, 75],
    [27, 96, 71, 94, 82],
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]

DESCRICOES_CICLO = [
    "Conexão inicial com satélite NASA POWER",
    "Estabilização da janela de coleta",
    "Interferência atmosférica detectada",
    "Degradação do canal de comunicação",
    "Tentativa de realinhamento do link satelital",
    "Restabelecimento do link e normalização",
]


def linha(char="─", tam=62, cor=CINZA):
    print(cor + char * tam + RESET)


def analisar_temperatura(valor):
    if valor > 35:
        return "CRÍTICO", VERMELHO, "Risco de superaquecimento", 2
    elif valor > 30 or valor < 18:
        return "ATENÇÃO", AMARELO, "Temperatura elevada", 1
    return "NORMAL", VERDE, "Temperatura estável", 0


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", VERMELHO, "Comunicação com a base em nível crítico", 2
    elif valor < 60:
        return "ATENÇÃO", AMARELO, "Comunicação instável", 1
    return "NORMAL", VERDE, "Comunicação estável", 0


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", VERMELHO, "Bateria em nível crítico", 2
    elif valor < 50:
        return "ATENÇÃO", AMARELO, "Bateria abaixo do recomendado", 1
    return "NORMAL", VERDE, "Energia estável", 0


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", VERMELHO, "Oxigênio em nível crítico", 2
    elif valor < 90:
        return "ATENÇÃO", AMARELO, "Oxigênio abaixo do ideal", 1
    return "NORMAL", VERDE, "Oxigênio adequado", 0


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", VERMELHO, "Estabilidade operacional crítica", 2
    elif valor < 70:
        return "ATENÇÃO", AMARELO, "Estabilidade operacional reduzida", 1
    return "NORMAL", VERDE, "Estabilidade operacional adequada", 0


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL", VERDE
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO", AMARELO
    return "MISSÃO CRÍTICA", VERMELHO


def gerar_recomendacao(analises):
    criticos = [areas_monitoradas[i] for i, (status, *_) in enumerate(analises) if status == "CRÍTICO"]
    atencoes = [areas_monitoradas[i] for i, (status, *_) in enumerate(analises) if status == "ATENÇÃO"]

    if not criticos and not atencoes:
        return "Manter operação normal e continuar monitoramento."

    msgs = []
    for area in criticos:
        if "Temperatura" in area:
            msgs.append("verificar sistema de dissipação térmica do módulo receptor")
        elif "Comunicação" in area:
            msgs.append("redirecionar para antena de backup e verificar link satelital")
        elif "energia" in area:
            msgs.append("acionar fonte de backup — geração solar insuficiente")
        elif "oxigênio" in area.lower():
            msgs.append("acionar protocolo de suporte de vida do módulo orbital")
        elif "Estabilidade" in area:
            msgs.append("reduzir operações não essenciais da estação receptora")

    if len(criticos) >= 3:
        return "Protocolo de emergência: acionar backup energético e restabelecer link com o módulo orbital."
    if msgs:
        return msgs[0].capitalize() + "."
    return "Monitorar sistemas em atenção e preparar plano de contingência."


def analisar_tendencia(pontuacoes):
    primeira = pontuacoes[0]
    ultima = pontuacoes[-1]
    if ultima > primeira:
        return "A missão apresentou tendência de piora.", VERMELHO
    elif ultima < primeira:
        return "A missão apresentou tendência de melhora.", VERDE
    return "A missão permaneceu estável em relação ao início.", AMARELO


def identificar_area_mais_afetada(pontuacoes_por_area):
    idx = pontuacoes_por_area.index(max(pontuacoes_por_area))
    return areas_monitoradas[idx], pontuacoes_por_area[idx]


def gerar_relatorio_final(pontuacoes_ciclos, pontuacoes_por_area, todas_analises, todos_dados):
    print()
    linha("═", 62, MAGENTA)
    print(MAGENTA + BOLD + "  RELATÓRIO FINAL DA MISSÃO" + RESET)
    linha("═", 62, MAGENTA)

    n = len(pontuacoes_ciclos)
    print(f"\n  {BOLD}Missão:{RESET}  {NOME_MISSAO}")
    print(f"  {BOLD}Equipe:{RESET}  {NOME_EQUIPE}")
    print(f"  {BOLD}Ciclos analisados:{RESET}  {n}")

    medias = []
    rotulos = ["Temperatura (°C)", "Comunicação (%)", "Bateria (%)", "Oxigênio (%)", "Estabilidade (%)"]
    for col in range(5):
        vals = [todos_dados[i][col] for i in range(n)]
        medias.append(sum(vals) / n)

    print()
    for i, rot in enumerate(rotulos):
        print(f"  {CINZA}{rot:<22}{RESET} {medias[i]:.1f}")

    ciclo_mais_critico = pontuacoes_ciclos.index(max(pontuacoes_ciclos)) + 1
    risco_medio = sum(pontuacoes_ciclos) / n
    ciclos_criticos = sum(1 for p in pontuacoes_ciclos if p >= 6)

    print(f"\n  {BOLD}Ciclo mais crítico:{RESET}   Ciclo {ciclo_mais_critico}  (pontuação {max(pontuacoes_ciclos)})")
    print(f"  {BOLD}Risco médio:{RESET}          {risco_medio:.2f}")
    print(f"  {BOLD}Ciclos críticos:{RESET}      {ciclos_criticos}/{n}")

    tendencia_msg, cor_tend = analisar_tendencia(pontuacoes_ciclos)
    print(f"\n  {BOLD}Tendência da missão:{RESET}")
    print(f"  {cor_tend}{tendencia_msg}{RESET}")

    print(f"\n  {BOLD}Pontuação acumulada por área:{RESET}")
    for i, area in enumerate(areas_monitoradas):
        pts = pontuacoes_por_area[i]
        cor = VERDE if pts <= 2 else (AMARELO if pts <= 5 else VERMELHO)
        print(f"  {CINZA}{area:<30}{RESET} {cor}{pts} pontos{RESET}")

    area_afetada, pts_area = identificar_area_mais_afetada(pontuacoes_por_area)
    print(f"\n  {BOLD}Área mais afetada:{RESET}  {MAGENTA}{area_afetada}{RESET}  ({pts_area} pontos)")

    class_final, cor_final = classificar_ciclo(risco_medio)
    print(f"\n  {BOLD}Classificação final:{RESET}  {cor_final}{BOLD}{class_final}{RESET}")

    print()
    linha("─", 62, CINZA)
    if ciclos_criticos == 0:
        conclusao = f"{VERDE}Missão dentro dos parâmetros. Nenhum ciclo crítico detectado.{RESET}"
    elif ciclos_criticos >= n // 2:
        conclusao = f"{VERMELHO}Missão em risco elevado. Intervenção imediata recomendada.{RESET}"
    else:
        conclusao = f"{AMARELO}Missão com instabilidades pontuais. Manter plano de contingência ativo.{RESET}"
    print(f"  {BOLD}Conclusão:{RESET} {conclusao}")
    linha("═", 62, MAGENTA)
    print()


def main():
    print()
    linha("═", 62, CIANO)
    print(CIANO + BOLD + "  ☀  MISSION CONTROL AI" + RESET)
    print(CINZA  + f"  Missão: {NOME_MISSAO}  |  Equipe: {NOME_EQUIPE}" + RESET)
    print(CINZA  + f"  Ciclos a analisar: {len(dados_missao)}" + RESET)
    linha("═", 62, CIANO)
    print()
    time.sleep(0.6)

    pontuacoes_ciclos = []
    pontuacoes_por_area = [0] * 5
    todas_analises = []

    for i, dado in enumerate(dados_missao):
        temp, comm, bat, ox, estab = dado
        desc = DESCRICOES_CICLO[i]

        analises = [
            analisar_temperatura(temp),
            analisar_comunicacao(comm),
            analisar_bateria(bat),
            analisar_oxigenio(ox),
            analisar_estabilidade(estab),
        ]

        pontuacao = sum(pts for *_, pts in analises)
        for j, (*_, pts) in enumerate(analises):
            pontuacoes_por_area[j] += pts

        classificacao, cor_class = classificar_ciclo(pontuacao)
        recomendacao = gerar_recomendacao(analises)

        pontuacoes_ciclos.append(pontuacao)
        todas_analises.append(analises)

        linha("─", 62, AZUL)
        print(f"  {BOLD}CICLO {i+1}{RESET}  —  {CINZA}{desc}{RESET}")
        linha("─", 62, AZUL)

        valores = [temp, comm, bat, ox, estab]
        unidades = ["°C", "%", "%", "%", "%"]
        rotulos = ["Temperatura", "Comunicação", "Bateria", "Oxigênio", "Estabilidade"]
        for j, (status, cor, msg, _) in enumerate(analises):
            print(
                f"  {CINZA}{rotulos[j]:<14}{RESET} "
                f"{valores[j]:>5}{unidades[j]}  "
                f"{cor}{BOLD}{status:<8}{RESET}  "
                f"{CINZA}{msg}{RESET}"
            )

        print(f"\n  {BOLD}Pontuação de risco:{RESET}  {pontuacao}")
        print(f"  {BOLD}Classificação:{RESET}       {cor_class}{BOLD}{classificacao}{RESET}")
        print(f"  {BOLD}Recomendação:{RESET}        {recomendacao}")
        print()
        time.sleep(0.2)

    gerar_relatorio_final(pontuacoes_ciclos, pontuacoes_por_area, todas_analises, dados_missao)


if __name__ == "__main__":
    main()
