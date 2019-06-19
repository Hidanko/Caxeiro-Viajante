from random import shuffle

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
geracoes = 50
num_populacoes = 5
# taxa de mutacao: 2 = 2%
mutacao = 2
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
print(str(num_cidades)+ ' cidades ')

cidades = alfabeto[0:num_cidades]

cont = 0
for obj in objetos[1:num_cidades+1]:
    arestas.append(Aresta(cont, cont+1, obj))
    cont = cont+1

#for obj in objetos[num_cidades+1:]:
    # gerar arestas em direções aleatórias com valores que sobraram

# for a in arestas:
#    print(a.destino)
populacao = list
populacao_peso = list
modelo = [[i] for i in range(num_cidades-1)]

for p in num_populacoes:
    shuffle(modelo)
    populacao.append(modelo)
    populacao_peso.append(-1)

nova_geracao = list
for geracao in range(0, geracoes):
    for p in populacao:
        flag_geral = True
        for pp in range(populacao.__sizeof__()-1):
            flag = False
            for a in arestas:
                if a.origem == populacao[pp] and a.destino == populacao[pp]:
                    flag = True
                    break
            if flag == False:
                flag_geral = False
            else:
                nova_geracao.append(populacao)

