import pandas as pd
import matplotlib.pyplot as plt
import os

# Caminho para o ficheiro CSV
csv_file = "output/log_data_aggregated.csv"

# Carrega os dados do CSV para um DataFrame
data = pd.read_csv(csv_file)

output_dir = "./figures"

# 1. Gráfico de Progresso do Download ao Longo do Tempo
plt.figure(figsize=(10, 6))
plt.plot(data.index, data["Progresso"], label="Progresso (%)", marker='o')
plt.xlabel("Tempo (Pontos de Amostra)")
plt.ylabel("Progresso (%)")
plt.title("Progresso do Download")
plt.legend()
plt.grid(True)

# Salva o gráfico no diretório especificado
output_path = os.path.join(output_dir, "grafico_progresso.png")
plt.savefig(output_path)
plt.show()

print(f"O gráfico foi guardado em: {output_path}")