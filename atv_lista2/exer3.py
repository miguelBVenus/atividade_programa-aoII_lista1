while True:
    operacao = input("digite S se quiser fazer a soma e N se nao quiser: ").upper()
    print(f"voce digitou {operacao}")
    if operacao == "N":
        print("voce escolheu sair do programa")
        break
    elif operacao != "S":
        print("Operação inválida.")
        continue
    numero = float(input("digite um numero:"))
    numero2 = float(input("digite outro numero:"))
    adicao = numero + numero2
    print("a soma deu:", adicao)