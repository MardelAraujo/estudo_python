def criar_album(artista,album):
    musica = {'O nome do artista é': artista, 'O nome do album é': album}
    return musica

musica01 = criar_album('Alee', 'Antes do Caos')
musica02 = criar_album('TZ da Coro', 'Dacoromode')
musica03 = criar_album('Chorão', 'Vicios e Virtudes')

print(musica01)
print(musica02) 