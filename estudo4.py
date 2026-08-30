nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f"sua media e {media} voce foi aprovado")
elif media == 10:
    print(f"sua media e {media} voce foi aprovado com distinção")
else:
    print(f"sua media e {media} voce foi reprovado")