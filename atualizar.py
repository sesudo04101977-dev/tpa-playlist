# Mapeamento com os links oficiais completos da infraestrutura de vídeo
CANAIS = {
    "TPA 1 HD": "https://live-video.net",
    "TPA 2 HD": "https://live-video.net",
    "TPA Notícias HD": "https://live-video.net"
}

conteudo_m3u = "#EXTM3U\n\n"

for nome, link_direto in CANAIS.items():
    # Monta a estrutura correta da playlist M3U linha por linha
    conteudo_m3u += f"#EXTINF:-1, {nome}\n{link_direto}\n\n"

# Grava a playlist final sem erros de texto
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(conteudo_m3u)

print("Playlist corrigida e estruturada com sucesso!")
