import pandas as pd
import matplotlib.pyplot as plt
import os
import json

# Caminho para o ficheiro CSV
csv_file = "output/scene1/log_data_aggregated1_2.csv"
output_dir = "./figures/scene1"

# Caminho para o ficheiro JSON
json_file = "./logs/cenario1/stats1_2.json"

data = pd.read_csv(csv_file)

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
plt.xlabel("Tempo")
plt.ylabel("Progresso (%)")
plt.title(f"Progresso do Download ao Longo do Tempo (Tempo Total: {tempo_total:.1f}s)")
plt.legend()
plt.grid(True)

# Salva o gráfico no diretório especificado
output_path = os.path.join(output_dir, "grafico_progresso2.png")
plt.savefig(output_path)
plt.show()


##################################################################################
################ 2. Evolução do Download e da sua velocidade #####################
##################################################################################

# Ordena os dados pelo tempo
data = data.sort_values(by="Tempo").reset_index(drop=True)

# Gráfico de Velocidade de Download ao Longo do Tempo
plt.figure(figsize=(12, 6))
plt.plot(data["Tempo"], data["Download"], color="blue", linewidth=2, label="Velocidade")

# Configurações do gráfico
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade do Download (Mbps)")
plt.title("Evolução da Velocidade de Download ao Longo do Tempo (Ordenado por Tempo)")
plt.legend()
plt.grid(True)  

# Salva o gráfico
output_path = os.path.join(output_dir, "grafico_velocidade_download2.png")
plt.savefig(output_path)
plt.show()


##################################################################################
#################### 3. Volume total de dados  ###################################
##################################################################################


# Carregar os dados do JSON
with open(json_file, "r") as file:
    data = json.load(file)

# Extrair valores de `uploaded-bytes` e `downloaded-bytes`
downloaded = data.get("downloaded-bytes", 0) / (1024 ** 2)  # Converte para MB
uploaded = data.get("uploaded-bytes", 0) / (1024 ** 2)  # Converte para MB
total = downloaded + uploaded  # Soma total em MB

# Preparar dados para o gráfico
labels = ["Downloaded", "Uploaded", "Total"]
values = [downloaded, uploaded, total]

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=["blue", "green", "orange"])
plt.title("Bytes Downloaded, Uploaded e Total (MB)")
plt.ylabel("MB")
plt.xlabel("Categoria")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Salvar o gráfico
output_path = os.path.join(output_dir, "grafico_bytes2.png")
plt.savefig(output_path)
plt.show()
