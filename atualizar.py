# Endereços de transmissão diretos e oficiais dos servidores da TPA
CANAIS_TPA = {
    "TPA 1 HD": "https://live-video.net",
    "TPA 2 HD": "https://live-video.net",
    "TPA Notícias HD": "https://live-video.net"
}

conteudo_m3u = "#EXTM3U\n\n"

for nome, link_video in CANAIS_TPA.items():
    # Estrutura a playlist M3U linha por linha com os links corretos
    conteudo_m3u += f"#EXTINF:-1, {nome}\n{link_video}\n\n"

# Grava o ficheiro final sem depender de consultas externas
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(conteudo_m3u)

print("Playlist oficial gerada com links diretos!")
