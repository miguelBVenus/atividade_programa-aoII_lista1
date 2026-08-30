n = int(input("Digite a quantidade de números: "))

i = 0
soma = 0

while i < n:
    numero = float(input("Digite um número entre 0 e 1000: "))

    while numero < 0 or numero > 1000:
        print("Valor inválido!")
        numero = float(input("Digite um número entre 0 e 1000: "))

    if i == 0:
        menor = numero
        maior = numero
    else:
        if numero < menor:
            menor = numero

        if numero > maior:
            maior = numero

    soma += numero
    i += 1

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Soma dos valores:", soma)