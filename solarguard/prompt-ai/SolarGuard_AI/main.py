dados_missao = [
    {"ciclo": 1, "irradiancia": 850, "temperatura": 29, "bateria": 90, "nuvens": 10, "estabilidade": 95},
    {"ciclo": 2, "irradiancia": 700, "temperatura": 32, "bateria": 75, "nuvens": 25, "estabilidade": 88},
    {"ciclo": 3, "irradiancia": 500, "temperatura": 36, "bateria": 60, "nuvens": 50, "estabilidade": 75},
    {"ciclo": 4, "irradiancia": 300, "temperatura": 40, "bateria": 40, "nuvens": 75, "estabilidade": 55},
    {"ciclo": 5, "irradiancia": 180, "temperatura": 44, "bateria": 25, "nuvens": 90, "estabilidade": 35},
    {"ciclo": 6, "irradiancia": 120, "temperatura": 47, "bateria": 15, "nuvens": 95, "estabilidade": 20}
]

for ciclo in dados_missao:

    indice = dados_missao.index(ciclo)

    if indice == 0:

        tendencia = "Sem histórico anterior para comparação."

    else:

        ciclo_anterior = dados_missao[indice - 1]

        if (
            ciclo["bateria"] < ciclo_anterior["bateria"]
            and ciclo["irradiancia"] < ciclo_anterior["irradiancia"]
            and ciclo["nuvens"] > ciclo_anterior["nuvens"]
        ):

            tendencia = (
                "Piora operacional: bateria em queda, "
                "irradiância menor e aumento de nuvens."
            )

        elif ciclo["bateria"] < ciclo_anterior["bateria"]:

            tendencia = (
                "Atenção: bateria em queda em relação ao ciclo anterior."
            )

        else:

            tendencia = (
                "Estável: sem piora relevante em relação ao ciclo anterior."
            )

    if ciclo["bateria"] < 30 or ciclo["estabilidade"] < 40:

        status = "Crítico"

        nivel_risco = "ALTO"

        motivo = "Bateria muito baixa ou estabilidade comprometida."

        recomendacao = (
            "Acionar modo de economia, reduzir consumo "
            "e usar fonte de backup."
        )

    elif (
        ciclo["irradiancia"] < 400
        or ciclo["nuvens"] > 70
        or ciclo["temperatura"] > 40
    ):

        status = "Atenção"

        nivel_risco = "MÉDIO"

        motivo = (
            "Baixa irradiância, muitas nuvens "
            "ou temperatura elevada."
        )

        recomendacao = (
            "Monitorar geração solar e preparar "
            "carregamento preventivo da bateria."
        )

    else:

        status = "Normal"

        nivel_risco = "BAIXO"

        motivo = "Todos os indicadores estão dentro dos níveis seguros."

        recomendacao = "Manter operação normal do sistema."

    analise_ia = f"""
Análise da missão SolarGuard:

Status: {status}
Nível de risco: {nivel_risco}
Temperatura: {ciclo['temperatura']}°C
Bateria: {ciclo['bateria']}%
Irradiância: {ciclo['irradiancia']} W/m²
Nuvens: {ciclo['nuvens']}%
Estabilidade: {ciclo['estabilidade']}%
Tendência: {tendencia}

Gere uma análise inteligente e uma recomendação técnica.
"""

    if status == "Crítico":

        resposta_ia = (
            f"A missão apresenta risco crítico. "
            f"A bateria está em {ciclo['bateria']}%, "
            f"a temperatura está em {ciclo['temperatura']}°C "
            f"e a cobertura de nuvens chegou a {ciclo['nuvens']}%. "
            f"Recomenda-se ativar o sistema de backup, "
            f"reduzir o consumo energético "
            f"e priorizar cargas essenciais."
        )

    elif status == "Atenção":

        resposta_ia = (
            f"A missão está em estado de atenção. "
            f"A irradiância atual é de "
            f"{ciclo['irradiancia']} W/m², "
            f"a temperatura está em "
            f"{ciclo['temperatura']}°C "
            f"e a cobertura de nuvens está em "
            f"{ciclo['nuvens']}%. "
            f"Recomenda-se monitorar a geração solar "
            f"e preparar carregamento preventivo da bateria."
        )

    else:

        resposta_ia = (
            f"A missão opera normalmente. "
            f"A irradiância está em "
            f"{ciclo['irradiancia']} W/m², "
            f"a bateria está em "
            f"{ciclo['bateria']}% "
            f"e a estabilidade está em "
            f"{ciclo['estabilidade']}%. "
            f"Recomenda-se manter a operação padrão do sistema."
        )

    print("\n" + "=" * 60)
    print(f"CICLO {ciclo['ciclo']} - SOLARGUARD AI")
    print("=" * 60)

    print(f"Status: {status}")
    print(f"Nível de risco: {nivel_risco}")
    print(f"Motivo: {motivo}")
    print(f"Tendência: {tendencia}")
    print(f"Recomendação: {recomendacao}")

    print("\nPrompt gerado:")
    print(analise_ia)

    print("Resposta da IA:")
    print(resposta_ia)