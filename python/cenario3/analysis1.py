import pandas as pd
import matplotlib.pyplot as plt
import os
import json

# Caminho para o ficheiro CSV
csv_file = "output/scene3/log_data_aggregated1_3.csv"
output_dir = "./figures/scene3"
    
# Caminho para o ficheiro JSON
json_file = "./logs/cenario3/stats1_5.json"

# Nomes para os gráficos individuais
graph_name_1 = "grafico_progresso3.png"
graph_name_2 = "grafico_velocidade_download3.png"
graph_name_3 = "grafico_bytes3.png"

# Nome para o gráfico agregado
graph_name_4 = "grafico_aggregated.png"

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
output_path = os.path.join(output_dir, graph_name_1)
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
plt.plot(data["Tempo"], data["Peers Conectados"], color="orange", linewidth=2, label="Peers Conectados")

# Configurações do gráfico
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade do Download (MB/s)")
plt.title("Evolução da Velocidade de Download ao Longo do Tempo (Ordenado por Tempo)")
plt.legend()
plt.grid(True)  

# Salva o gráfico
output_path = os.path.join(output_dir, graph_name_2)
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
print(values)

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=["blue", "green", "orange"])
plt.title("Bytes Downloaded, Uploaded e Total (MB)")
plt.ylabel("MB")
plt.xlabel("Categoria")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Salvar o gráfico
output_path = os.path.join(output_dir, graph_name_3)
plt.savefig(output_path)
plt.show()



##################################################################################
############# 4. Gráfico da Velocidade do Download ao Longo do Tempo ##############
##################################################################################

file_1= "output/scene3/log_data_aggregated1_1.csv"
file_2= "output/scene3/log_data_aggregated1_2.csv"
file_3= "output/scene3/log_data_aggregated1_3.csv"

data_1 = pd.read_csv(file_1)
data_2 = pd.read_csv(file_2)
data_3 = pd.read_csv(file_3)

# Ordena os dados pelo tempo
data_1 = data_1.sort_values(by="Tempo").reset_index(drop=True)
data_2 = data_2.sort_values(by="Tempo").reset_index(drop=True)
data_3 = data_3.sort_values(by="Tempo").reset_index(drop=True)

# Calculo da média do tempo e download para os 3
mean_time_1 = data_1["Tempo"].mean()
mean_time_2 = data_2["Tempo"].mean()
mean_time_3 = data_3["Tempo"].mean()

mean_dl_1 = data_1["Download"].mean()
mean_dl_2 = data_2["Download"].mean()
mean_dl_3 = data_3["Download"].mean()

print(mean_time_1, mean_time_2, mean_time_3)
print(mean_dl_1, mean_dl_2, mean_dl_3)

# Gráfico de Velocidade de Download ao Longo do Tempo
plt.figure(figsize=(12, 6))
plt.plot(data_1["Tempo"], data_1["Download"], color="blue", linewidth=2, label="1a Iteração")
plt.plot(data_2["Tempo"], data_2["Download"], color="red", linewidth=2, label="2a Iteração")
plt.plot(data_3["Tempo"], data_3["Download"], color="green", linewidth=2, label="3a Iteração")

# Configurações do gráfico
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade do Download (Mbps)")
plt.title("Evolução da Velocidade de Download ao Longo do Tempo (Ordenado por Tempo) das 3 simulações")
plt.legend()
plt.grid(True)  

# Salva o gráfico
output_path = os.path.join(output_dir, graph_name_4)
plt.savefig(output_path)
plt.show()

