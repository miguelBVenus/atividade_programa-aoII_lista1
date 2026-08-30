numero1 = int(input("digite um numero:"))
numero2 = int(input("digite outro numero:"))
numero3 = int(input("digite mais um numero:"))
if numero1 > numero2 and numero1 > numero3:
    print(f"o numero {numero1} e o maior")
elif numero2 > numero1 and numero2 > numero3:
    print(f"o numero {numero2} e o maior")
else:
    print(f"o numero {numero3} e o maior")