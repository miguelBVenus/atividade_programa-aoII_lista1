numero = int(input("Digite um número inteiro: "))

divisores = 0
i = 1

while i <= numero:
    if numero % i == 0:
        divisores += 1
    i += 1

if divisores == 2:
    print("O número é primo.")
else:
    print("O número não é primo.")

