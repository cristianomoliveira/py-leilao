from dominio import Usuario, Lance, Leilao, Avaliador




for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de: {lance.valor}')


avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior foi {avaliador.maior_lance}')
