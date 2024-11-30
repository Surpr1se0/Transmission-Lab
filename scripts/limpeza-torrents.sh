#!/bin/bash

TRANS_DIR="/home/surprise/.config/transmission"
DOWNLOAD_DIR="/home/surprise/Downloads"

DIRS_TO_CLEAN=(
    "$TRANS_DIR/resume/"
    "$TRANS_DIR/torrents/"
    "$DOWNLOAD_DIR/"
)

echo "[DEBUG] Limpar conteúdo das pastas"
for DIR in "${DIRS_TO_CLEAN[@]}"; do
    if [ -d "$DIR" ]; then
        rm -rf "$DIR"/*
        echo "[DEBUG] Conteúdo de $DIR limpo."
    else
        echo "[DEBUG] Diretório $DIR não encontrado, ignorando."
    fi
done

