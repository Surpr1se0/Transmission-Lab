import pandas as pd
import csv
from collections import defaultdict

# Caminho para o CSV
input_file = "./output/scene2/log_data_1_1.csv"
output_file = "./output/scene2/log_data_aggregated1_1.csv"

# Lê os dados do CSV
data = pd.read_csv(input_file)

# Função para converter velocidades de kB/s para MB/s
def convert_to_mbs(speed):
    if "kB/s" in speed:
        return float(speed.replace("kB/s", "").strip()) / 1000  # kB/s para MB/s
    elif "MB/s" in speed:
        return float(speed.replace("MB/s", "").strip())  # Mantém MB/s inalterado
    return 0

# Aplica a conversão na coluna `Download` antes de agregar
data["Download"] = data["Download"].apply(convert_to_mbs)

# Agrupa os dados por `Tempo` e calcula médias ou valores relevantes para cada coluna
aggregated_data = (
    data.groupby("Tempo", as_index=False)
    .agg({
        "Progresso": lambda x: x.iloc[0],  # Mantém o primeiro valor para `Progresso`
        "Peers Conectados": lambda x: x.iloc[0],  # Mantém o primeiro valor para `Peers Conectados`
        "Peers Totais": "mean",  # Calcula a média de `Peers Totais`
        "Download": "max",  # Usa o valor máximo de `Download` (em MB/s)
        "Upload": lambda x: x.max(),  # Usa o valor máximo de `Upload`
    })
)

# Converte a coluna `Upload` para string (caso necessário)
aggregated_data["Upload"] = aggregated_data["Upload"].astype(str)

# Salva o CSV com os dados agregados
aggregated_data.to_csv(output_file, index=False)

print(f"Dados agregados guardados no ficheiro: {output_file}")
