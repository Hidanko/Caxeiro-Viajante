from random import shuffle

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

# def sorteio_roleta(populacao):
#     #populacao
#
def get_cidades(tamanho):
    return alfabeto[0:tamanho-1]

def get_primeiras_populacoes(tamanho, tamanho_populacao):
    modelo =  alfabeto[0:tamanho-1]
    populacao = [tamanho_populacao]
    for p in range(0, tamanho_populacao):
        m = list(modelo)
        print('antes:' + str(m))
        shuffle(m)
        print('depois shuffle:' + str(m))
        populacao.append(m)
        # populacao_peso.append(int(-1))

        return populacao