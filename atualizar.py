import requests
import re

# Canais oficiais da TPA e as suas páginas de transmissão direta
CANAIS_TPA = {
    "TPA 1 HD": "https://tpa.ao",
    "TPA 2 HD": "https://tpa.ao",
    "TPA Notícias HD": "https://tpa.ao"
}

conteudo_m3u = "#EXTM3U\n\n"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

for nome, url_pagina in CANAIS_TPA.items():
    try:
        response = requests.get(url_pagina, headers=headers, timeout=15)
        if response.status_code == 200:
            # Captura o link direto .m3u8 do leitor de vídeo da página
            match = re.search(r'(https://[^"\']+\.m3u8[^"\']*)', response.text)
            if match:
                playback_url = match.group(1)
                conteudo_m3u += f"#EXTINF:-1, {nome}\n{playback_url}\n\n"
                print(f"Sucesso: {nome} obtido.")
                continue
        print(f"Não foi possível extrair o sinal para: {nome}")
    except Exception as e:
        print(f"Erro no canal {nome}: {e}")

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(conteudo_m3u)
