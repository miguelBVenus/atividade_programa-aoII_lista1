while True:
    turno = input("digite o turno que voce estuda (M/V/N): ").upper()

    if turno == "M":
      print("bom dia")
      break 
    elif turno == "V":
      print("boa tarde")
      break
    elif turno == "N":
      print("boa noite")
      break
    else:
      print("valor invalido, digite M, V ou N")