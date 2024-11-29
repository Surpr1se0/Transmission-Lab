#!/bin/bash

# Diretórios
TORRENT_DIR="./torrents"
LOG_DIR="./logs"

# Certifica-te de que os diretórios existem
mkdir -p "$TORRENT_DIR"
mkdir -p "$LOG_DIR"

# Caminho para o ficheiro .torrent
TORRENT_FILE="$TORRENT_DIR/ubuntu.torrent"

# Nome do ficheiro de log RAW
LOG_FILE_RAW="$LOG_DIR/cenario1_raw.log"

# Verifica se o ficheiro .torrent existe
if [ ! -f "$TORRENT_FILE" ]; then
    echo "Erro: O ficheiro .torrent não foi encontrado em $TORRENT_FILE."
    exit 1
fi

# Regista a hora de início
START_TIME=$(date +%s)

# Inicia o download e guarda os logs no ficheiro RAW
echo "Iniciando o download do torrent..."
transmission-cli "$TORRENT_FILE" | tee "$LOG_FILE_RAW" | while read -r line; do
    # Verifica se o download foi concluído
    if echo "$line" | grep -q "Progress: 100.0%"; then
        echo "Download completo! A encerrar o Transmission CLI..."
        pkill transmission-cli
        break
    fi
done

# Regista a hora de término
END_TIME=$(date +%s)

# Calcula o tempo total de download
TOTAL_TIME=$((END_TIME - START_TIME))

# Exibe e regista as métricas finais
echo "Tempo total de download: $TOTAL_TIME segundos"
echo "Logs RAW disponíveis em: $LOG_FILE_RAW"

