import pandas as pd
import matplotlib.pyplot as plt
import os
import json

# Caminho para os ficheiros CSV e JSON
csv_file = "output/scene1/log_data_aggregated1_1.csv"
output_dir = "./figures/scene1"
json_file = "./logs/cenario1/stats1_2.json"

# Cria diretório para salvar gráficos
os.makedirs(output_dir, exist_ok=True)

# Leitura dos dados do CSV
data = pd.read_csv(csv_file)

# Tempo total
tempo_total = data["Tempo"].max()

##################################################################################
############# 1. Gráfico de Progresso do Download ao Longo do Tempo ##############
##################################################################################

plt.figure(figsize=(12, 6))
plt.plot(data["Tempo"], data["Progresso"], label="Progresso (%)", color="blue", linewidth=2)

# Anotações
plt.scatter(data["Tempo"].iloc[0], data["Progresso"].iloc[0], color="green", label="Início")
plt.scatter(data["Tempo"].iloc[-1], data["Progresso"].iloc[-1], color="red", label="Final")

# Configurações do gráfico
plt.xlabel("Tempo (s)")
plt.ylabel("Progresso (%)")
plt.title(f"Progresso do Download ao Longo do Tempo (Tempo Total: {tempo_total:.1f}s)")
plt.legend()
plt.grid(True)

# Salva o gráfico no diretório especificado
output_path = os.path.join(output_dir, "grafico_progresso1.png")
plt.savefig(output_path)
plt.show()

##################################################################################
############# 2. Gráfico de Overhead (Ficheiro vs Dados Transferidos) ############
##################################################################################

# Carregar os dados do JSON
with open(json_file, "r") as file:
    json_data = json.load(file)

# Extrair valores do JSON
downloaded = json_data.get("downloaded-bytes", 0) / (1024 ** 2)  # Convertido para MB
uploaded = json_data.get("uploaded-bytes", 0) / (1024 ** 2)  # Convertido para MB
total_transferidos = downloaded + uploaded

tamanho_ficheiro = 3300

# Gráfico de Barras
labels = ["Tamanho do Ficheiro", "Total Transferido"]
values = [tamanho_ficheiro, total_transferidos]

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=["green", "blue"])
plt.title("Overhead: Tamanho do Ficheiro vs Dados Transferidos")
plt.ylabel("Volume (MB)")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Salvar o gráfico
output_path = os.path.join(output_dir, "grafico_overhead1.png")
plt.savefig(output_path)
plt.show()

