n = 0
c = 0
s = 0
while True:
    n = int(input('Digite um valor, ou 999 para parar: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foi digitado {c} números e a soma total foi {s}')