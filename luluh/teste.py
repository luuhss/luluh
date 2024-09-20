lista = []
penultimo = []


contagem = 10
contador = 9
multiplicador = 10


cpf=input("Digite um cpf:")
cpf=cpf.replace(".","")
cpf=cpf.replace("-","")



if len(cpf) == 11 and cpf.isdigit():


  for c in range (2):

    lista.clear()

    for i in range (contador):
      dígito = int(cpf[i])
      resultado = dígito * contagem
      lista.append(resultado)
      contagem -=1

    resultado = sum(lista)

    resultado = resultado % 11
    resultado = 11 - resultado

    contagem = 11
    contador = 10

    penultimo.append(resultado)

  if penultimo[0] == int(cpf[9]) and penultimo[1] == int(cpf[10]):
    print("CPF Válido")
  else:
    print("CPF Inválido")

else:
  print("CPF Inválido")
