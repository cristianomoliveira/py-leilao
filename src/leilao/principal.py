from dominio import Usuario, Lance, Leilao


user1 = Usuario('Cristiano')
user2 = Usuario('Astolfo')

lance_user1 = Lance(user1, 100.0)
lance_user2 = Lance(user2, 200.0)

leilao = Leilao('Notebook')

leilao.lances.append(lance_user1)
leilao.lances.append(lance_user2)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de: {lance.valor}')