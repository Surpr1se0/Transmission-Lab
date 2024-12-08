#!/bin/bash

# Diretórios
TORRENT_DIR="$(dirname $(dirname $(pwd)))/Transmission-Lab/torrents"
LOG_DIR="$(dirname $(pwd))/logs/cenario1"

# Certifica-te de que os diretórios existem
mkdir -p "$TORRENT_DIR"
mkdir -p "$LOG_DIR"

# Caminho para o ficheiro .torrent
TORRENT_FILE="$TORRENT_DIR/ubuntu.torrent"

# Nome do ficheiro de log RAW com timestamps
LOG_FILE_RAW="$LOG_DIR/cenario3_1raw.log"

# Verifica se o ficheiro .torrent existe
if [ ! -f "$TORRENT_FILE" ]; then
    echo "Erro: O ficheiro .torrent não foi encontrado em $TORRENT_FILE."
    exit 1
fi

# Regista a hora de início e outras mensagens de debug
echo "[DEBUG] Script iniciado às $(date '+%Y-%m-%d %H:%M:%S')"
echo "[DEBUG] Logs serão armazenados em $LOG_FILE_RAW"
echo "[DEBUG] Caminho do ficheiro .torrent: $TORRENT_FILE"

# Inicia o download e captura a saída, transformando as atualizações em linhas separadas
echo "[DEBUG] Iniciando o download do torrent..."
transmission-cli "$TORRENT_FILE" 2>&1 | stdbuf -oL tr '\r' '\n' | while IFS= read -r line; do
    # Adiciona um timestamp antes de cada linha
    TIMESTAMPED_LINE="$(date '+%Y-%m-%d %H:%M:%S') $line"
    echo "$TIMESTAMPED_LINE" >> "$LOG_FILE_RAW"
    # echo "[DEBUG] Capturado: $TIMESTAMPED_LINE"

    # Verifica se o download foi concluído
    if echo "$line" | grep -q "Progress: 100.0%"; then
        #echo "[DEBUG] Detetado progresso de 100%."
        #echo "Download completo! A encerrar o Transmission CLI..."
        pkill transmission-cli
        break
    fi
done

