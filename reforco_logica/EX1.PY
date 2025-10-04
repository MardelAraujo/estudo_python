"""def mostrar_mensagem(spm):

    print(f"Olá galera, neste super modulo estou aprendendo {spm}")


mostrar_mensagem("Função")"""

'''def livro_favorito(titulo_livro):

    print(f"Um dos meus livros favoritos é {titulo_livro}")

livro_favorito("Eu fico loko")'''

def fazer_camiseta(tamanho,texto):

    return f'A camisa é do tamanho {tamanho} e está estampado {texto}.'

camisa01 = fazer_camiseta("G", "Python é foda, java é fodinha")
camisa02 = fazer_camiseta(texto="ele é gay", tamanho="M")

print(camisa01)
print(camisa02)