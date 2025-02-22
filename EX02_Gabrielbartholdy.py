produto = ('tv','maquina lavar','celular','cadeira','movel','cama','estante','mesa de centro','monitor','pc gamer')

print(produto)

searprod = input("Escolha um dos produtos no estoque acima: ")

if searprod in produto:

    posi = produto.index(searprod)
    print('posicao {}'.format(posi))
 
perg2 = int(input('informe um numero de 0 a 9 para exibir um produto da lista: '))

if 0 <= perg2 < len(produto):
    print('o produto é: {}'.format(produto[perg2]))

