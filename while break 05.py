tgasto = preço2 = pmil = cont = 0
produtobar = ''
continuar = ''
while True :
    if continuar == 'N' :
        break
    np = str(input('Digite o nome do produto comprado: '))
    preço = int(input('Digite o preço do produto comprado: '))
    cont += 1
    tgasto += preço
    if preço > 1000 :
        pmil += 1
    if cont == 1 or preço < preço2 :
        preço2 = preço
        produtobar = np
    continuar = str(input('Digite S para continuar ou N para parar: ')).strip().upper()
print(f'O total gasto foi R${tgasto}, {pmil} produtos custaram mais do que 1000 R$, {produtobar} é o produto mais barato custando {preço2}.')