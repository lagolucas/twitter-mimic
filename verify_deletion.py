import comparador
import database
import twitter


def verify(arrobas):
    for arroba in arrobas:
        print(arroba)
        lista_atual = twitter.get_all(arroba)

        lista_antiga = database.recupera_ids(arroba)

        apagados = comparador.compara(lista_antiga, lista_atual)