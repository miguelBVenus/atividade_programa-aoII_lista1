contador = 0
resposta = input("telefone para a vitima? (S/N): ").upper()
if resposta.upper() == "S":
    contador += 1
resposta = input("esteve no local do crime? (S/N):").upper()
if resposta.upper() == "S":
    contador += 1
resposta = input("mora perto da vitima? (S/N): ").upper()
if resposta.upper() == "S":
    contador +=1 
resposta = input("devia para a vitima? (S/N):").upper()
if resposta.upper() == "S":
    contador += 1
resposta = input("ja trabalhou com a vitima? (S/N): ").upper()
if resposta.upper() == "S":
    contador +=1 

if contador == 2:
    print("voce e suspeito")
elif contador >= 3 and contador <= 4:
    print("voce e cumplice")
elif contador >=5:
    print("voce e o assasino")
else:
    print("voce e inocente")
    