import pandas as pd
import json 
import os
# Nomes dos ficheiros
file_names = ['output/scene2/log_data_aggregated2_1.csv', 
              'output/scene2/log_data_aggregated2_2.csv', 
              'output/scene2/log_data_aggregated2_3.csv']

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

        # Converter colunas para numérico (se necessário)
        df['Tempo'] = pd.to_numeric(df['Tempo'], errors='coerce')
        df['Peers Conectados'] = pd.to_numeric(df['Peers Conectados'], errors='coerce')
        df['Download'] = pd.to_numeric(df['Download'], errors='coerce')
        df['Upload'] = pd.to_numeric(df['Upload'], errors='coerce')

        # Remover linhas com valores inválidos (NaN)
        df = df.dropna(subset=['Tempo', 'Peers Conectados', 'Download', 'Upload'])

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

######################################
############ VER OS JSONS ############
######################################

# Lista com os nomes dos ficheiros JSON
files = ["logs/cenario2/stats2_1.json", 
         "logs/cenario2/stats2_2.json", 
         "logs/cenario2/stats2_3.json"]

# Inicializar somatórios
sum_downloaded = 0
sum_uploaded = 0
sum_seconds_active = 0
sum_files_added = 0
sum_session_count = 0
file_count = len(files)

# Processar cada ficheiro JSON
for file in files:
    if os.path.exists(file):
        with open(file, "r") as f:
            data = json.load(f)
            sum_downloaded += data.get("downloaded-bytes", 0)
            sum_uploaded += data.get("uploaded-bytes", 0)
            sum_seconds_active += data.get("seconds-active", 0)
            sum_files_added += data.get("files-added", 0)
            sum_session_count += data.get("session-count", 0)
    else:
        print(f"Ficheiro não encontrado: {file}")

# Calcular médias
if file_count > 0:
    avg_downloaded = sum_downloaded / file_count
    avg_uploaded = sum_uploaded / file_count
    avg_seconds_active = sum_seconds_active / file_count
    avg_files_added = sum_files_added / file_count
    avg_session_count = sum_session_count / file_count

    # Exibir resultados
    print("Médias calculadas:")
    print(f"Média de bytes descarregados: {avg_downloaded:.2f}")
    print(f"Média de bytes enviados: {avg_uploaded:.2f}")
    print(f"volume total de dados: {avg_uploaded+avg_downloaded:.2f}")
    print(f"Média de segundos ativos: {avg_seconds_active:.2f}")
    print(f"Média de ficheiros adicionados: {avg_files_added:.2f}")
    print(f"Média de contagem de sessões: {avg_session_count:.2f}")
else:
    print("Nenhum ficheiro foi processado.")
