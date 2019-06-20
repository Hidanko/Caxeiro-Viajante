from random import shuffle, randint


class Aresta:
    origem = -1
    destino = -1
    peso = -1

    def __init__(self, origem, destino, peso):
        self.origem = origem
        self.destino = destino
        self.peso = peso


# Caminho para o txt
txt = 'C:/Users/Sattra/Documents/str-integracoes/endpoints - Poly/dist/movimentacoes/teste.txt'
geracoes = 30
num_populacoes = 5
# taxa de mutacao: 2 = 2%
mutacao = 2
num_mutacoes = 1
# Alfabeto com 20 caracteres para representar até 20 cidades
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
arestas = []
arquivo = open(txt)
print(arquivo.read())

arquivo = open(txt)
objetos = arquivo.read().split(';')

num_cidades = int(objetos[0])
# Limitar em 20 cidades
if num_cidades > 20:
    raise Exception('Numero de cidades inválido')
print(str(num_cidades) + ' cidades ')

cidades = alfabeto[0:num_cidades]

cont = 0
for obj in objetos[1:num_cidades + 1]:
    arestas.append(Aresta(cont, cont + 1, obj))
    # Correcao para aresta ser bidirecional
    arestas.append(Aresta(cont + 1, cont, obj))
    cont = cont + 1

# for obj in objetos[num_cidades+1:]:
# gerar arestas em direções aleatórias com valores que sobraram

# for a in arestas:
#    print(a.destino)
populacao = list
populacao_peso = list
modelo = [[i] for i in range(num_cidades - 1)]

for p in range(0, num_populacoes):
    print('antes:' + str(modelo))
    shuffle(modelo)
    print('depois shuffle:' + str(modelo))
    populacao.append(list(modelo))
    populacao_peso.append(int(-1))

nova_geracao = list
for geracao in range(0, geracoes):
    for p in populacao:
        flag_geral = True
        for pp in range(populacao.__sizeof__() - 1):
            flag = False
            for a in arestas:
                if a.origem == populacao[pp] and a.destino == populacao[pp]:
                    flag = True
                    break
            if not flag:
                flag_geral = False
            else:
                nova_geracao.append(populacao)

        # POSSIVEL LOOP
        parente1 = nova_geracao[randint(0, nova_geracao.__sizeof__() - 1)]
        parente2 = nova_geracao[randint(0, nova_geracao.__sizeof__() - 1)]
        filho = list
        # gerar filho a partir dos parentes
        for valor in range(0, int(num_cidade / 2)):
            filho.append(parente1[valor])

        for valor in range(0, int((num_cidade / 2) if num_cidades % 2 == 0 else (num_cidades / 2 - 1))):
            filho.append(parente2[valor])
        # else = exception
        if filho.__sizeof__() == num_cidades:
            nova_geracao.append(filho)

    if mutacao <= randint(0, 100):
        for n in range(0, num_mutacoes):
            g_rand = nova_geracao.__sizeof__()
            v_rand = randint(0, num_cidades)
            g_rand2 = nova_geracao.__sizeof__()
            v_rand2 = randint(0, num_cidades)
            temp = nova_geracao[randint(0, g_rand)][v_rand]
            temp2 = nova_geracao[randint(0, g_rand2)][v_rand2]
            nova_geracao[randint(0, g_rand)][v_rand] = temp2
            nova_geracao[randint(0, g_rand2)][v_rand2] = temp1

    populacao = nova_geracao

    # FITNESS

index = -1
peso = 999
for p in populacao:
    temp_peso = 0
    for pp in range(populacao.__sizeof__() - 1):
        flag = False
        for a in arestas:
            if a.origem == populacao[pp] and a.destino == populacao[pp]:
                temp_peso = temp_peso + a.peso
                flag = True
        # Caso não encontre um caminho
            if not flag:
                temp_peso = 999999
    if temp_peso < peso:
        peso = temp_peso
        index = pp

print('MENOR CAMINHO:')
print(populacao[index])
