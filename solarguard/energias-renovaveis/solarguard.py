# =============================================================
#   SolarGuard — Monitoramento Energético Solar
#   Missão Espacial Experimental
#   Global Solution 2026.1 — SERS
#   Grupo 5 | Turma 1CCPY | FIAP
# =============================================================
#   Integrantes:
#   Matheus da Costa Gonçalves     — RM 570756
#   Jair Ferreira dos Santos Neto  — RM 569682
#   Yan Luiz Neves Lemos           — RM 571717
# =============================================================

import matplotlib.pyplot as plt

dados_missao = [
    [1,  850, 600, 28, 90],
    [2,  720, 620, 30, 85],
    [3,  530, 650, 32, 78],
    [4,  310, 680, 35, 65],
    [5,  180, 700, 38, 50],
    [6,   90, 720, 41, 35],
    [7,  650, 600, 33, 40],
    [8,  780, 590, 29, 55],
    [9,  900, 580, 27, 70],
    [10, 860, 600, 28, 82],
]

AREA_PAINEL_M2      = 2.0   # área dos painéis solares (m²)
EFICIENCIA_PAINEL   = 0.18  # eficiência dos painéis fotovoltaicos (18%)
LIMIAR_IRRADIANCIA  = 400   # W/m² — abaixo disso: alerta de baixa geração
LIMIAR_BATERIA_CRIT = 40    # %    — abaixo disso: bateria crítica
LIMIAR_TEMP_CRITICA = 38    # °C   — acima disso: temperatura crítica nos painéis

def calcular_geracao(irradiancia):
    """Calcula a potência gerada pelos painéis solares (Watts)."""
    return irradiancia * AREA_PAINEL_M2 * EFICIENCIA_PAINEL

def verificar_alertas(irradiancia, consumo, temperatura, bateria, geracao):
    """Verifica condições críticas e retorna lista de alertas."""
    alertas = []

    if irradiancia < LIMIAR_IRRADIANCIA:
        alertas.append(
            f"⚠️  Irradiância baixa ({irradiancia:.0f} W/m²) — geração comprometida"
        )

    if geracao < consumo:
        deficit = consumo - geracao
        alertas.append(
            f"⚠️  Consumo ({consumo:.0f}W) supera geração ({geracao:.1f}W) "
            f"— déficit de {deficit:.1f}W"
        )

    if bateria < LIMIAR_BATERIA_CRIT:
        alertas.append(
            f"🔴 CRÍTICO: Bateria em {bateria}% — abaixo do limite seguro"
        )

    if temperatura > LIMIAR_TEMP_CRITICA:
        alertas.append(
            f"🌡️  Temperatura crítica nos painéis ({temperatura}°C)"
        )

    return alertas

def tomada_de_decisao(geracao, consumo, bateria, irradiancia):
    """Retorna a ação recomendada com base nas condições do ciclo."""
    if bateria < LIMIAR_BATERIA_CRIT and irradiancia < LIMIAR_IRRADIANCIA:
        return "🚨 AÇÃO: Acionar fonte de backup — bateria crítica e geração insuficiente"
    elif geracao > consumo * 1.2:
        return "🔋 AÇÃO: Superávit detectado — direcionar excedente para carga da bateria"
    elif geracao < consumo and bateria > 60:
        return "🔁 AÇÃO: Complementar com bateria — geração insuficiente temporária"
    elif irradiancia < LIMIAR_IRRADIANCIA:
        return "💡 AÇÃO: Ativar modo econômico — reduzir consumo não essencial"
    else:
        return "✅ AÇÃO: Sistema estável — operação normal"

def exibir_relatorio():
    """Processa todos os ciclos e exibe o relatório completo."""
    print("=" * 65)
    print("   🛸 SOLARGUARD — Monitoramento Energético Solar")
    print("   Missão Espacial Experimental | Grupo 5 — 1CCPY FIAP")
    print("=" * 65)

    geracoes = []
    consumos = []
    ciclos   = []
    baterias = []

    for dado in dados_missao:
        ciclo, irradiancia, consumo, temperatura, bateria = dado
        geracao = calcular_geracao(irradiancia)
        alertas = verificar_alertas(irradiancia, consumo, temperatura, bateria, geracao)
        acao    = tomada_de_decisao(geracao, consumo, bateria, irradiancia)

        print(f"\n📡 CICLO {ciclo:02d}")
        print(f"   Irradiância : {irradiancia} W/m²")
        print(f"   Geração     : {geracao:.1f} W")
        print(f"   Consumo     : {consumo} W")
        print(f"   Temperatura : {temperatura}°C")
        print(f"   Bateria     : {bateria}%")

        if alertas:
            for alerta in alertas:
                print(f"   {alerta}")
        else:
            print("   ✅ Nenhum alerta neste ciclo")

        print(f"   {acao}")
        print("-" * 65)

        geracoes.append(geracao)
        consumos.append(consumo)
        ciclos.append(ciclo)
        baterias.append(bateria)

    print("\n✅ Monitoramento concluído. Gerando visualização...\n")
    visualizar_curva(ciclos, geracoes, consumos, baterias)

def visualizar_curva(ciclos, geracoes, consumos, baterias):
    """Plota a curva de carga e o nível de bateria ao longo dos ciclos."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7))
    fig.suptitle(
        "SolarGuard — Curva de Carga da Missão Espacial",
        fontsize=14, fontweight='bold'
    )

    # Gráfico 1: Geração vs Consumo
    ax1.plot(ciclos, geracoes, 'o-',  color='gold',   label='Geração Solar (W)', linewidth=2)
    ax1.plot(ciclos, consumos, 's--', color='tomato',  label='Consumo (W)',       linewidth=2)

    ax1.fill_between(
        ciclos, geracoes, consumos,
        where=[g < c for g, c in zip(geracoes, consumos)],
        alpha=0.25, color='red',   label='Déficit energético'
    )
    ax1.fill_between(
        ciclos, geracoes, consumos,
        where=[g >= c for g, c in zip(geracoes, consumos)],
        alpha=0.2,  color='green', label='Superávit energético'
    )

    ax1.set_ylabel("Potência (W)")
    ax1.set_title("Geração Solar vs Consumo por Ciclo de Monitoramento")
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.set_xticks(ciclos)

    # Gráfico 2: Nível de Bateria
    cores_bateria = [
        'green'  if b > 60 else
        'orange' if b > LIMIAR_BATERIA_CRIT else
        'red'
        for b in baterias
    ]
    ax2.bar(ciclos, baterias, color=cores_bateria, edgecolor='black', linewidth=0.5)
    ax2.axhline(
        y=LIMIAR_BATERIA_CRIT, color='red', linestyle='--',
        label=f'Limite crítico ({LIMIAR_BATERIA_CRIT}%)'
    )

    ax2.set_xlabel("Ciclo de Monitoramento")
    ax2.set_ylabel("Nível de Bateria (%)")
    ax2.set_title("Nível de Bateria por Ciclo")
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.set_xticks(ciclos)
    ax2.set_ylim(0, 100)

    plt.tight_layout()
    plt.savefig("solarguard_curva_carga.png", dpi=150, bbox_inches='tight')
    plt.show()
    print("📊 Gráfico salvo como 'solarguard_curva_carga.png'")

if __name__ == "__main__":
    exibir_relatorio()
