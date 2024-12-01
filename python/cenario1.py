import re
import csv
from datetime import datetime

# Caminho para o log
log_file_path = "./logs/cenario1/cenario1_1raw.log"

# Escreve os dados no CSV
output_file = "./output/scene1/log_data_1.csv"

# Padrão de regex para extrair a informação
log_pattern = re.compile(
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) Progress:\s([\d.]+)%,\sdl\sfrom\s(\d+)\sof\s(\d+)\speers\s\(([\d.]+\s(?:kB/s|MB/s))\),\sul\sto\s(\d+)\s\(([\d.]+\s(?:kB/s|MB/s))\)"
)

# Armazenar os dados extraídos
data = []

with open(log_file_path, "r") as log_file: 
    for line in log_file: 
        match = log_pattern.search(line)
        if match:
            timestamp = match.group(1).split(" ")[1]  # Extrai apenas HH:MM:SS
            progress = float(match.group(2))
            peers_connected = int(match.group(3))
            peers_total = int(match.group(4))
            dl_speed = match.group(5)
            ul_speed = match.group(6)

            # Adiciona os dados extraídos à lista
            data.append({
                "Timestamp": timestamp,
                "Progresso": progress,
                "Peers Conectados": peers_connected,
                "Peers Totais": peers_total,
                "Download": dl_speed,
                "Upload": ul_speed
            })

# Converte o `Timestamp` em uma escala de tempo (segundos desde o início)
def convert_to_seconds(data):
    # Converte todos os timestamps para objetos datetime
    time_objects = [datetime.strptime(row["Timestamp"], "%H:%M:%S") for row in data]
    start_time = time_objects[0]  # Define o primeiro timestamp como referência
    for i, row in enumerate(data):
        elapsed_seconds = (time_objects[i] - start_time).total_seconds()
        row["Tempo"] = elapsed_seconds
        # Remove o campo `Timestamp` após usar
        del row["Timestamp"]
    return data

# Adiciona a coluna `Tempo (s)` e remove o `Timestamp`
data = convert_to_seconds(data)


with open(output_file, "w", newline="") as csv_file:
    fieldnames = ["Tempo", "Progresso", "Peers Conectados", "Peers Totais", "Download", "Upload"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Escreve o cabeçalho e os dados
    writer.writeheader()
    writer.writerows(data)

print(f"dados guardados no ficheiro {output_file}")
