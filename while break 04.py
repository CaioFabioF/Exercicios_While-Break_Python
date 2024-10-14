cp = 0
ch = 0
cmm = 0
cpm = 0
while True:
    c = int(input('Digite 1 para cadastrar, ou 2 para finalizar: '))
    if c == 2 :
        break
    s = str(input('Digite F para Feminino ou M para Masculino: ')).strip().upper()
    id = int(input('Digite a sua idade: '))
    cp += 1
    if s == 'F' :
        if id > 18 :
            cpm += 1
            if id < 20 :
                cmm += 1
    if s == 'M' :
        ch += 1
        if id > 18 :
            cpm += 1
print(f'A quantidade de pessoas cadastradas foi {cp}, a quantidade de mulheres menores de 20 anos foi {cmm}, são {ch} homens cadastrados, e {cpm} no total, são maiores de idade')