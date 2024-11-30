import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o ficheiro CSV
csv_file = "log_data.csv"

# Carrega os dados do CSV para um DataFrame
data = pd.read_csv(csv_file)

# 1. Gráfico de Progresso do Download ao Longo do Tempo
plt.figure(figsize=(10, 6))
plt.plot(data.index, data["Progresso"], label="Progresso (%)", marker='o')
plt.xlabel("Tempo (Pontos de Amostra)")
plt.ylabel("Progresso (%)")
plt.title("Progresso do Download")
plt.legend()
plt.grid(True)
plt.savefig("grafico_progresso.png")
plt.show()
