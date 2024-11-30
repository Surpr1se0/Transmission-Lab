import pandas as pd
import csv
from collections import defaultdict

# Caminho para o CSV
input_file = "./output/log_data.csv"
output_file = "./output/log_data_aggregated.csv"

# Lê os dados do CSV
data = pd.read_csv(input_file)

# Agrupa os dados por `Timestamp` e calcula médias para colunas numéricas
aggregated_data = (
    data.groupby("Tempo", as_index=False)
    .agg({
        "Progresso": lambda x:x.iloc[0],  
        "Peers Conectados": lambda x:x.iloc[0],  
        "Peers Totais": "mean",  
        "Download": lambda x: x.max(),
        "Upload": lambda x: x.max(), 
    })
)

# Converte as colunas `Download` e `Upload` para strings (caso necessário)
aggregated_data["Download"] = aggregated_data["Download"].astype(str)
aggregated_data["Upload"] = aggregated_data["Upload"].astype(str)

# Salva o CSV com os dados agregados
aggregated_data.to_csv(output_file, index=False)

print(f"Dados agregados guardados no ficheiro: {output_file}")
