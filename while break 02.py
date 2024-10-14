while True:
    n = int(input('Digite um número para ser tabuado: '))
    if n < 0 :
        break
    for c in range(1,11) :
        print(f'{n} x {c} é: {n*c}')
print('Tabuada encerrada')