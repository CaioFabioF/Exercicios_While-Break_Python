import random
v = 0
while True:
    c = random.randint(0,10)
    j = int(input('Digite um número de 0 até 10: '))
    total = c + j
    tipo = ' '
    while tipo not in 'PI' :
        tipo = str(input('Par ou Ímpar[P/I]? ')).strip().upper()[0]
    print(f'Você jogou {j} o computador jogou {c} e o total foi {total}')
    if tipo == 'P' :
        if total % 2 == 0 :
            print('Você venceu')
            v += 1
        else :
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar denovo')
print(f'Voce venceu {v} vezes!')
