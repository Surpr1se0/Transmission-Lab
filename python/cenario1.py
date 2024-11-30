import re
import csv

# Caminho para o log
log_file_path = "./logs/cenario1_raw.log"

# padrão de regex para tirar a info
log_pattern = re.compile(
      r"Progress:\s([\d.]+)%,\sdl\sfrom\s(\d+)\sof\s(\d+)\speers\s\(([\d.]+\s(?:kB/s|MB/s))\),\sul\sto\s(\d+)\s\(([\d.]+\s(?:kB/s|MB/s))\)"
)

# armazenar os dados extraídos
data = []

with open(log_file_path, "r") as log_file: 
  for line in log_file: 
    match = log_pattern.search(line)
    if match:
      progress = float(match.group(1))
      peers_connected = int(match.group(2))
      peers_total = int (match.group(3))
      dl_speed = match.group(4)
      ul_speed = match.group(5)

      # Adiciona os dados extraídos à lista
      data.append({
        "Progresso": progress,
        "Peers Conectados": peers_connected,
        "Peers Totais": peers_total,
        "Download": dl_speed,
        "Upload": ul_speed
        })

# Escreve os dados extraídos no CSV
output_file = "./output/log_data.csv"
with open(output_file, "w", newline="") as csv_file:
    fieldnames = ["Progresso", "Peers Conectados", "Peers Totais", "Download", "Upload"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Escreve o cabeçalho e os dados
    writer.writeheader()
    writer.writerows(data)

print(f"dados guardados no ficheiro {output_file}")