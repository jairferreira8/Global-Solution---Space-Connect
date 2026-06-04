import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from scipy import stats

ARQUIVO = "dataset.csv"
MESES = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]

df = pd.read_csv(ARQUIVO, parse_dates=["data"])
irrad = df["irradiancia_kwh_m2"]
mes   = df["mes"]

print("=" * 65)
print("  SOLARGUARD — Análise Estatística de Irradiância Solar")
print("  Fonte: NASA POWER API | São Paulo (SP) | 2023")
print("  Modelagem Linear para Aprendizado de Máquina — FIAP")
print("=" * 65)
print(f"\n  Registros carregados: {len(df)} dias  |  Período: 2023-01-01 a 2023-12-31\n")


# ── 1. Tabela de distribuição de frequências — variável discreta (mês) ─────

print("─" * 65)
print("  TABELA 1 — Distribuição de Frequências: Mês (variável discreta)")
print("─" * 65)

freq_mes = df.groupby("mes").size().reset_index(name="freq_abs")
freq_mes["freq_rel"]   = freq_mes["freq_abs"] / len(df)
freq_mes["freq_rel_p"] = freq_mes["freq_rel"] * 100
freq_mes["freq_ac"]    = freq_mes["freq_abs"].cumsum()
freq_mes["freq_ac_p"]  = freq_mes["freq_rel_p"].cumsum()
freq_mes["media_irrad"] = df.groupby("mes")["irradiancia_kwh_m2"].mean().values

print(f"\n  {'Mês':<6} {'Nome':<6} {'Fi':>5} {'Fr (%)':>8} {'Fac':>6} {'Fac (%)':>9} {'Média (kWh/m²)':>15}")
print("  " + "-" * 60)
for _, row in freq_mes.iterrows():
    m = int(row["mes"])
    print(f"  {m:<6} {MESES[m-1]:<6} {int(row['freq_abs']):>5} "
          f"{row['freq_rel_p']:>7.1f}% {int(row['freq_ac']):>6} "
          f"{row['freq_ac_p']:>8.1f}%  {row['media_irrad']:>13.2f}")
print(f"\n  Fi = frequência absoluta | Fr = frequência relativa | Fac = frequência acumulada\n")


# ── 2. Tabela de distribuição de frequências — variável contínua (irradiância) ─

print("─" * 65)
print("  TABELA 2 — Distribuição de Frequências: Irradiância (variável contínua)")
print("─" * 65)

k = int(1 + 3.322 * np.log10(len(irrad)))
amplitude_classe = (irrad.max() - irrad.min()) / k
bins = [irrad.min() + i * amplitude_classe for i in range(k + 1)]
bins[-1] += 0.01

rotulos = [f"{bins[i]:.2f} ├─ {bins[i+1]:.2f}" for i in range(k)]
freq_irrad, _ = np.histogram(irrad, bins=bins)
freq_rel_i    = freq_irrad / len(irrad) * 100
freq_ac_i     = np.cumsum(freq_irrad)
freq_ac_p_i   = np.cumsum(freq_rel_i)

print(f"\n  {'Classe (kWh/m²)':<22} {'Fi':>5} {'Fr (%)':>8} {'Fac':>6} {'Fac (%)':>9}")
print("  " + "-" * 55)
for i in range(k):
    print(f"  {rotulos[i]:<22} {freq_irrad[i]:>5} {freq_rel_i[i]:>7.1f}% "
          f"{freq_ac_i[i]:>6} {freq_ac_p_i[i]:>8.1f}%")
print(f"\n  Regra de Sturges: k = {k} classes | Amplitude de classe ≈ {amplitude_classe:.2f} kWh/m²\n")


# ── 3. Análise univariada — irradiância ────────────────────────────────────

print("─" * 65)
print("  ANÁLISE UNIVARIADA — Irradiância Solar Diária (kWh/m²/dia)")
print("─" * 65)

media    = irrad.mean()
mediana  = irrad.median()
moda_r   = stats.mode(irrad, keepdims=True)
moda_v   = moda_r.mode[0]
maximo   = irrad.max()
minimo   = irrad.min()
amplitude= maximo - minimo
variancia= irrad.var(ddof=1)
desvpad  = irrad.std(ddof=1)
cv       = (desvpad / media) * 100
q1       = irrad.quantile(0.25)
q2       = irrad.quantile(0.50)
q3       = irrad.quantile(0.75)
iqr      = q3 - q1

print(f"\n  Medidas de Tendência Central")
print(f"  {'Média':<28} {media:.4f} kWh/m²/dia")
print(f"  {'Mediana':<28} {mediana:.4f} kWh/m²/dia")
print(f"  {'Moda (aprox.)':<28} {moda_v:.4f} kWh/m²/dia")

print(f"\n  Medidas de Dispersão")
print(f"  {'Máximo':<28} {maximo:.4f} kWh/m²/dia")
print(f"  {'Mínimo':<28} {minimo:.4f} kWh/m²/dia")
print(f"  {'Amplitude':<28} {amplitude:.4f} kWh/m²/dia")
print(f"  {'Variância':<28} {variancia:.4f}")
print(f"  {'Desvio Padrão':<28} {desvpad:.4f} kWh/m²/dia")
print(f"  {'Coeficiente de Variação':<28} {cv:.2f}%")

print(f"\n  Medidas Separatrizes (Quartis)")
print(f"  {'Q1 (25%)':<28} {q1:.4f} kWh/m²/dia")
print(f"  {'Q2 — Mediana (50%)':<28} {q2:.4f} kWh/m²/dia")
print(f"  {'Q3 (75%)':<28} {q3:.4f} kWh/m²/dia")
print(f"  {'IQR (Q3 - Q1)':<28} {iqr:.4f} kWh/m²/dia")
print()


# ── 3b. Análise univariada — temperatura ──────────────────────────────────

print("─" * 65)
print("  ANÁLISE UNIVARIADA — Temperatura Diária (°C)")
print("─" * 65)

temp = df["temperatura_c"]

t_media     = temp.mean()
t_mediana   = temp.median()
t_moda_r    = stats.mode(temp, keepdims=True)
t_moda_v    = t_moda_r.mode[0]
t_maximo    = temp.max()
t_minimo    = temp.min()
t_amplitude = t_maximo - t_minimo
t_variancia = temp.var(ddof=1)
t_desvpad   = temp.std(ddof=1)
t_cv        = (t_desvpad / t_media) * 100
t_q1        = temp.quantile(0.25)
t_q2        = temp.quantile(0.50)
t_q3        = temp.quantile(0.75)
t_iqr       = t_q3 - t_q1

print(f"\n  Medidas de Tendência Central")
print(f"  {'Média':<28} {t_media:.4f} °C")
print(f"  {'Mediana':<28} {t_mediana:.4f} °C")
print(f"  {'Moda (aprox.)':<28} {t_moda_v:.4f} °C")

print(f"\n  Medidas de Dispersão")
print(f"  {'Máximo':<28} {t_maximo:.4f} °C")
print(f"  {'Mínimo':<28} {t_minimo:.4f} °C")
print(f"  {'Amplitude':<28} {t_amplitude:.4f} °C")
print(f"  {'Variância':<28} {t_variancia:.4f}")
print(f"  {'Desvio Padrão':<28} {t_desvpad:.4f} °C")
print(f"  {'Coeficiente de Variação':<28} {t_cv:.2f}%")

print(f"\n  Medidas Separatrizes (Quartis)")
print(f"  {'Q1 (25%)':<28} {t_q1:.4f} °C")
print(f"  {'Q2 — Mediana (50%)':<28} {t_q2:.4f} °C")
print(f"  {'Q3 (75%)':<28} {t_q3:.4f} °C")
print(f"  {'IQR (Q3 - Q1)':<28} {t_iqr:.4f} °C")
print()


# ── 4. Gráfico 1 — Irradiância média mensal (barras) ───────────────────────

media_mensal = df.groupby("mes")["irradiancia_kwh_m2"].mean()
cores = ["#e74c3c" if v < 3.5 else "#f39c12" if v < 5.0 else "#2ecc71" for v in media_mensal]

fig1, ax1 = plt.subplots(figsize=(12, 6))
barras = ax1.bar(range(1, 13), media_mensal.values, color=cores, edgecolor="white",
                  linewidth=0.8, zorder=3)

for bar, val in zip(barras, media_mensal.values):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.06,
             f"{val:.2f}", ha="center", va="bottom", fontsize=9, fontweight="bold", color="#333")

ax1.set_title("Irradiância Solar Média Mensal — São Paulo (2023)\nFonte: NASA POWER API",
              fontsize=14, fontweight="bold", pad=15)
ax1.set_xlabel("Mês", fontsize=12)
ax1.set_ylabel("Irradiância Média (kWh/m²/dia)", fontsize=12)
ax1.set_xticks(range(1, 13))
ax1.set_xticklabels(MESES, fontsize=10)
ax1.set_ylim(0, media_mensal.max() * 1.18)
ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.1f"))
ax1.axhline(media, color="#3498db", linestyle="--", linewidth=1.5,
            label=f"Média anual: {media:.2f} kWh/m²/dia", zorder=4)
ax1.grid(axis="y", alpha=0.35, zorder=0)
ax1.legend(fontsize=10)
ax1.spines[["top", "right"]].set_visible(False)

from matplotlib.patches import Patch
legenda_cores = [
    Patch(color="#e74c3c", label="Baixa (< 3,5 kWh/m²)"),
    Patch(color="#f39c12", label="Moderada (3,5 – 5,0 kWh/m²)"),
    Patch(color="#2ecc71", label="Alta (> 5,0 kWh/m²)"),
]
ax1.legend(handles=legenda_cores + [plt.Line2D([0], [0], color="#3498db", linestyle="--",
           label=f"Média anual: {media:.2f} kWh/m²/dia")],
           fontsize=9, loc="upper left")

plt.tight_layout()
plt.savefig("grafico1_irradiancia_mensal.png", dpi=150, bbox_inches="tight")
plt.show()
print("  Gráfico 1 salvo: grafico1_irradiancia_mensal.png")


# ── 5. Gráfico 2 — Histograma da distribuição de irradiância diária ────────

fig2, ax2 = plt.subplots(figsize=(11, 6))

n, bin_edges, patches = ax2.hist(irrad, bins=k, color="#3498db", edgecolor="white",
                                  linewidth=0.7, alpha=0.85, zorder=3)

for patch, left in zip(patches, bin_edges):
    centro = left + amplitude_classe / 2
    if centro < 3.5:
        patch.set_facecolor("#e74c3c")
    elif centro < 5.0:
        patch.set_facecolor("#f39c12")
    else:
        patch.set_facecolor("#2ecc71")

ax2.axvline(media,   color="#2c3e50",  linestyle="-",  linewidth=2,
            label=f"Média: {media:.2f}")
ax2.axvline(mediana, color="#8e44ad",  linestyle="--", linewidth=2,
            label=f"Mediana: {mediana:.2f}")
ax2.axvline(q1,      color="#95a5a6",  linestyle=":",  linewidth=1.5,
            label=f"Q1: {q1:.2f}")
ax2.axvline(q3,      color="#95a5a6",  linestyle=":",  linewidth=1.5,
            label=f"Q3: {q3:.2f}")

ax2.set_title("Distribuição de Frequência — Irradiância Solar Diária\nSão Paulo, 2023 (n = 365 dias)",
              fontsize=14, fontweight="bold", pad=15)
ax2.set_xlabel("Irradiância (kWh/m²/dia)", fontsize=12)
ax2.set_ylabel("Frequência (dias)", fontsize=12)
ax2.legend(fontsize=10)
ax2.grid(axis="y", alpha=0.35, zorder=0)
ax2.spines[["top", "right"]].set_visible(False)

plt.tight_layout()
plt.savefig("grafico2_histograma_irradiancia.png", dpi=150, bbox_inches="tight")
plt.show()
print("  Gráfico 2 salvo: grafico2_histograma_irradiancia.png")

print("\n" + "=" * 65)
print("  Análise concluída.")
print("=" * 65 + "\n")
