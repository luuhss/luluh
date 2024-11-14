
lista = []

for i in range(3):
    while True:
        Digt = input("Digite um Numero: ")
        if Digt.isdigit()== True:
            Digt= int(Digt)
            lista.append(Digt)
            break
        else: 
            print("Erro, Não é um Número")

   

for a in lista:
    for b in lista:
        for c in lista:
            print(a, b, c)
