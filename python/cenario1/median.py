import pandas as pd
import os

# Nomes dos ficheiros
file_names = ['output/scene1/log_data_aggregated1_1.csv', 
              'output/scene1/log_data_aggregated1_2.csv', 
              'output/scene1/log_data_aggregated1_3.csv']

# Inicialização das variáveis para cálculo das médias
total_tempo = 0
total_pares_conectados = 0
total_download = 0
total_upload = 0
total_linhas = 0

# Iterar sobre cada ficheiro
for file_name in file_names:
    if os.path.exists(file_name):
        # Ler o ficheiro CSV
        df = pd.read_csv(file_name)
        
        # Somar as colunas relevantes
        total_tempo += df['Tempo'].iloc[-1]  # Último valor do tempo indica o tempo total
        total_pares_conectados += df['Peers Conectados'].mean()  # Média dos pares conectados
        total_download += df['Download'].mean()  # Média da velocidade de download
        total_upload += df['Upload'].mean()  # Média da velocidade de upload
        total_linhas += 1
    else:
        print(f"Ficheiro não encontrado: {file_name}")

# Cálculo das médias gerais
if total_linhas > 0:
    media_tempo = total_tempo / total_linhas
    media_pares_conectados = total_pares_conectados / total_linhas
    media_download = total_download / total_linhas
    media_upload = total_upload / total_linhas

    # Exibição dos resultados
    print(f"Média do tempo demorado: {media_tempo:.2f} segundos")
    print(f"Média dos pares conectados: {media_pares_conectados:.2f}")
    print(f"Média da velocidade de download: {media_download:.2f} MB/s")
    print(f"Média da velocidade de upload: {media_upload:.2f} MB/s")
else:
    print("Nenhum ficheiro foi encontrado ou processado.")