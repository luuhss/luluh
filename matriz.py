def Matiz ():
    matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    soma_total = 0
    
    for i in range      (3):
        print('')
        for a in range(3):
            print(f"{matriz[i][a]}  ", end= '')
    for linha in matriz:
        soma_total += sum(linha)
    print(soma_total)
Matiz()   