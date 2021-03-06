from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador

class TestAvaliador(TestCase):
    
    #caso de uso (situação) e Retorno
    def test_quando_adicionados_em_ordem_crescente_deve_retorar_o_maior_e_o_menor_de_um_lance(self):
        user1 = Usuario('Cristiano')
        user2 = Usuario('Astolfo')

        lance_user2 = Lance(user2, 100.0)
        lance_user1 = Lance(user1, 150.0)
        

        leilao = Leilao('Notebook')

        leilao.lances.append(lance_user2)
        leilao.lances.append(lance_user1)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0


        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)

        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)



    def test_quando_adicionados_em_ordem_decrescente_deve_retorar_o_maior_e_o_menor_de_um_lance(self):
        user1 = Usuario('Cristiano')
        user2 = Usuario('Astolfo')

        lance_user1 = Lance(user1, 150.0)
        lance_user2 = Lance(user2, 100.0)

        leilao = Leilao('Notebook')

        leilao.lances.append(lance_user2)
        leilao.lances.append(lance_user1)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0


        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)

        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)


    def test_quando_leilao_tiver_um_lance_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance(self):

        user1 = Usuario('Cristiano')
        
        lance_user1 = Lance(user1, 150.0)
        

        leilao = Leilao('Notebook')

        leilao.lances.append(lance_user1)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(150.0, avaliador.menor_lance)
        self.assertEqual(150.0, avaliador.maior_lance)



    def test_quando_o_leilao_tiver_3_lances_deve_retorar_o_maior_e_o_menor_lance(self):
        user1 = Usuario('Cristiano')
        user2 = Usuario('Astolfo')
        user3 = Usuario('Maria')

        lance_user1 = Lance(user1, 150.0)
        lance_user2 = Lance(user2, 100.0)
        lance_user3 = Lance(user3, 200.0)

        leilao = Leilao('Notebook')

        leilao.lances.append(lance_user1)
        leilao.lances.append(lance_user2)
        leilao.lances.append(lance_user3)
        

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0


        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)

        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)




