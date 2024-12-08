import matplotlib.pyplot as plt
import numpy as np
import os

# Caminhos para salvar os gráficos
output_dir = "figures"
os.makedirs(output_dir, exist_ok=True)

# Dados fornecidos
cenarios = ["Cenário 1", "Cenário 2", "Cenário 3"]

# Dados
total_dados_ubuntu = [3355.80, 2798.66, 3169.35]
total_dados_kali = [2818.14, 3337.69, 3331.40]

volume_download_ubuntu = [3.44, 2.06, 2.83]
volume_download_kali = [4.58, 7.56, 6.03]

tempos_ubuntu = [330.67, 1068.00, 2074.00]
tempos_kali = [288.67, 886.67, 2510.00]

# Configuração do eixo X
x = np.arange(len(cenarios))  # Posições das barras
width = 0.35  # Largura das barras

### 1. Comparação do Volume Total de Dados (Download + Upload) ###
fig, ax = plt.subplots(figsize=(10, 6))
bars_ubuntu = ax.bar(x - width/2, total_dados_ubuntu, width, label="Ubuntu", color="blue")
bars_kali = ax.bar(x + width/2, total_dados_kali, width, label="Kali", color="orange")

ax.set_xlabel("Cenários")
ax.set_ylabel("Volume Total de Dados (MB)")
ax.set_title("Comparação do Volume Total de Dados (Download + Upload)")
ax.set_xticks(x)
ax.set_xticklabels(cenarios)
ax.legend()

for bar in bars_ubuntu:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=9)
for bar in bars_kali:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=9)

plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig(f"{output_dir}/volume_total_comparacao.png")
plt.show()

### 2. Comparação do Volume de Download ###
fig, ax = plt.subplots(figsize=(10, 6))
bars_ubuntu = ax.bar(x - width/2, volume_download_ubuntu, width, label="Ubuntu", color="blue")
bars_kali = ax.bar(x + width/2, volume_download_kali, width, label="Kali", color="orange")

ax.set_xlabel("Cenários")
ax.set_ylabel("Volume de Download (MB)")
ax.set_title("Comparação do Volume de Download")
ax.set_xticks(x)
ax.set_xticklabels(cenarios)
ax.legend()

for bar in bars_ubuntu:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=9)
for bar in bars_kali:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=9)

plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig(f"{output_dir}/volume_download_comparacao.png")
plt.show()

### 3. Comparação dos Tempos de Transferência ###
fig, ax = plt.subplots(figsize=(10, 6))
bars_ubuntu = ax.bar(x - width/2, tempos_ubuntu, width, label="Ubuntu", color="blue")
bars_kali = ax.bar(x + width/2, tempos_kali, width, label="Kali", color="orange")

ax.set_xlabel("Cenários")
ax.set_ylabel("Duração (s)")
ax.set_title("Comparação dos Tempos de Transferência")
ax.set_xticks(x)
ax.set_xticklabels(cenarios)
ax.legend()

for bar in bars_ubuntu:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=9)
for bar in bars_kali:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=9)

plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig(f"{output_dir}/tempos_comparacao.png")
plt.show()