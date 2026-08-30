n = int(input("digite a quantidade de numeros:"))

i = 0
soma = 0

while i < n:
    numero = float(input("digite um numero:"))

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

print("O menor numero é:", menor)
print("O maior numero é:", maior)
print("A soma dos numeros é:", soma)