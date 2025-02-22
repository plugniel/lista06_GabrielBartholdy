
festa = []

for contador in range(0, 3):
    convidado_festa = input('Digite o nome da pessoa que deseja convidar para a festa: ')
    festa.append(convidado_festa)

quantfesta = input('Você convidou {} pessoas, deseja convidar mais pessoas? s/n:'.format(festa)).lower()
if quantfesta == 's':
    while True:
        convidado_festa = input('Digite o nome da pessoa que deseja convidar para a festa: ')
        festa.append(convidado_festa)
        quantfesta = input('Deseja convidar mais pessoas? s/n:')
        if quantfesta == 'n':
            break
        else:
            break
else:
    print('continue')
print(festa)

Nomelista = input(' digite um nome da lista: ')

if Nomelista in festa:
    Clista = festa.index(Nomelista)
    print('A Pessoa convidada esta na posição "{}"'.format(Clista))
    Compafesta = input('Ainda deseja que ele venha na festa? s/n: ')
    if Compafesta == 's':
        print('perfeito ')
    elif Compafesta == 'n':
        festa.remove(Compafesta)
        print(festa)

print('gabriel Bartholdy')