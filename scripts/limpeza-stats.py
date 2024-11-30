import json
import os

# Caminho para o ficheiro stats.json
stats_file = os.path.expanduser("~/.config/transmission/stats.json")

def reset_stats(file_path):
    # Verifica se o ficheiro existe
    if not os.path.exists(file_path):
        print(f"[ERRO] O ficheiro '{file_path}' não foi encontrado.")
        return

    # Lê o conteúdo atual do ficheiro
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"[ERRO] O ficheiro '{file_path}' não contém JSON válido.")
        return

    # Redefine os valores a 0
    for key in data.keys():
        data[key] = 0

    # Grava o novo conteúdo no ficheiro
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"[INFO] Os dados do ficheiro '{file_path}' foram redefinidos para 0.")

# Executa a função
if __name__ == "__main__":
    reset_stats(stats_file)

