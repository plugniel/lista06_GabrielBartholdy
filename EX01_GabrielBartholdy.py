#EXE 001 . - Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.

paises = ('russia', 'chile', 'bresai', 'Estados Unidos', 'espanha')
print(paises)

paiscee = input('Digite um pais que esta na lista: ')


if paiscee in paises:
    paise = paises.index(paiscee)
    print('O pais "{}" esta na lista e esta na indice "{}"'.format(paiscee, paise))
else:
    print('País não está na lista')
print('gabriel Bartholdy')