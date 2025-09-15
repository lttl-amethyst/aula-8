def consumo_combustivel():
    nome = input("digite seu nome: ")
    info1 = float(input("digite a quantidade de quilômetros percorridos: "))
    info2 = float(input("digite a quantidade de litros de combustível gasto: "))

    consumo = (info1/info2)
    if consumo >= 15:
        situacao = "O consumo foi econômico"
    elif consumo >= 10 and consumo <= 14.9:
        situacao = "O consumo foi regular"
    elif consumo < 10:
        situacao = "O consumo foi alto"

    print(f"\nNome: {nome}")
    print(f"\nConsumo: {consumo}")
    print(f"\nSituação: {situacao}")

consumo_combustivel()


def imc():
    nome = input("digite seu nome: ")
    info1 = float(input("digite seu peso: "))
    info2 = float(input("digite sua altura: "))

    imc = (info1/(info2*2))
    if imc < 18.5:
        situacao = "abaixo do peso"
    elif imc == 18.5 and imc <= 24.9: 
        situacao = "peso regular"
    elif imc == 25 and imc <= 29.9:
        situacao = "sobrepeso"
    elif imc >= 30:
        situacao = "obesidade"

    print(f"\nnome: {nome}")
    print(f"\nimc: {imc}")
    print(f"\nsituação: {situacao}")

imc()


def velocidade():
    nome = input("digite seu nome: ")
    info1 = float(input("digite sua velocidade registrada: "))

    velo = 80
    if info1 >= velo:
        situacao = "dentro do limite"
    elif info1 == 81 and info1 <= 100: 
        situacao = "acima do limite"
    elif info1 > 100:
        situacao = "acima do limite"

    print(f"\nnome: {nome}")
    print(f"\nlimite de velocidade: {velo}")
    print(f"\nsituação: {situacao}")

velocidade()


def soma():
    nome = input("difite seu nome: ")
    info1 = float (input("digite um número: "))
    info2 = float (input("digite outro número: "))

    soma = info1 + info2
    print(f"\no resultado da soma é: {soma}")

soma()