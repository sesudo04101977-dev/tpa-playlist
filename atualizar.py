python
import json
import requests

# IDs estáveis dos canais da TPA na infraestrutura Kick/Amazon
CANAIS = {
    "TPA 1 HD": "NkqBWoO9PHkr",
    "TPA 2 HD": "RVhWHai4kSxM",
    "TPA Notícias HD": "BjjqJlEj3H3p"
}

conteudo_m3u = "#EXTM3U\n\n"

# Cabeçalhos para simular um navegador comum e evitar bloqueios
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

for nome, channel_id in CANAIS.items():
    url = f"https://kick.com{channel_id}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Extrai o link .m3u8 que já vem com o token dinâmico atualizado
            playback_url = data["livestream"]["playback_url"]
            conteudo_m3u += f"#EXTINF:-1, {nome}\n{playback_url}\n\n"
            print(f"Sucesso: {nome} atualizado.")
        else:
            print(f"Erro {response.status_code} no canal {nome}")
    except Exception as e:
        print(f"Falha ao ligar ao canal {nome}: {e}")

# Guarda o resultado num ficheiro local que o GitHub vai publicar
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(conteudo_m3u)
