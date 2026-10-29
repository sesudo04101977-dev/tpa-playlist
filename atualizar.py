# Códigos de transmissão estáveis dos canais da TPA na Amazon IVS
CANAIS = {
    "TPA 1 HD": "NkqBWoO9PHkr",
    "TPA 2 HD": "RVhWHai4kSxM",
    "TPA Notícias HD": "BjjqJlEj3H3p"
}

conteudo_m3u = "#EXTM3U\n\n"

for nome, channel_id in CANAIS.items():
    # Estruturação direta do endereço do servidor de distribuição de vídeo da Amazon IVS
    playback_url = f"https://live-video.net.{channel_id}.m3u8"
    conteudo_m3u += f"#EXTINF:-1, {nome}\n{playback_url}\n\n"

# Gravação da lista estruturada
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(conteudo_m3u)

print("Playlist direta estruturada com sucesso!")
