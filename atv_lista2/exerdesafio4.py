

nome = input("Digite seu nome: ")

while len(nome) <= 3:
    print("Nome inválido! Digite um nome com mais de 3 caracteres.")
    nome = input("Digite seu nome: ")


idade = int(input("Digite sua idade: "))

while idade < 0 or idade > 150:
    print("Idade inválida! Digite uma idade entre 0 e 150.")
    idade = int(input("Digite sua idade: "))



salario = float(input("Digite seu salário: "))

while salario <= 0:
    print("Salário inválido! Digite um valor maior que zero.")
    salario = float(input("Digite seu salário: "))



sexo = input("Digite seu sexo (m/f): ").lower()

while sexo != "m" and sexo != "f":
    print("Sexo inválido! Digite m ou f.")
    sexo = input("Digite seu sexo (m/f): ").lower()



estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()

while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    print("Estado civil inválido! Digite s, c, v ou d.")
    estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()


print("\nInformações válidas!")
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado civil:", estado_civil)

