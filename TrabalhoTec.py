import PySimpleGUI as sg
sg.theme('Dark gray 8')
def Bv():
    # Tela de Bem-Vindo
    layout = [  [sg.Text("clique em 'Começa' para começar experiencia ou clique em 'Login' para fazer cadastro")],
                [sg.Button('Começa'), sg.Button('Quero ser membro')] ]

        # Criador de janela
    window = sg.Window('Bem-Vindo!', layout)

        
    while True:
        event, values = window.read()

            # condição para o usuario fechar o programa
        if event == sg.WIN_CLOSED:
            break
        if event == 'Quero ser membro':
            window.close()
            Membro()
        elif event == 'Começa':
            window.close()
            Nota()
    window.close()

def Membro():
    layout = [  [sg.Text("Clique em cadastre-se para ser um novo membro")],
                [sg.Text('Ja é membro? Clique em login')],
                [sg.Button('Login'), sg.Button('Cadastre-se')] ]

        # Criador de janela
    window = sg.Window('Seja Membro!!', layout)

        
    while True:
        event, values = window.read()

            # condição para o usuario fechar o programa
        if event == sg.WIN_CLOSED:
            break
        if event == 'Cadastre-se':
            window.close()
            Cadastro()
        elif event == 'Login':
            window.close()
            Login()
    window.close()

def Login():
    layout = [  [sg.Text('Nome do usuario: ')],
                [sg.InputText(key='nombre')],
                [sg.Text('Digite sua senha: ')],
                [sg.InputText(key='chave')],
                [sg.Button('Entrar')] ]

    window = sg.Window('Que bom te ver de novo:)', layout)

        
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == "Entrar":
            nombre = values ['nombre'] 
            chave= values ['chave']
            if nombre.isdigit():
                sg.popup ('Erro: Seu nome é numerico')   
            elif nombre == '' and chave == '':
                sg.popup("Erro: os espaços estão vazios")
            elif len(nombre) <= 3:
                sg.popup('Erro: Nome não é valido')
            elif not chave.isdigit():
                sg.popup('Erro: Sua senha so pode ser numerica')
        else:
            window.close()
            Bv()
    window.close()

def Cadastro():
    erros = ''

    layout = [  
        [sg.Text('Digite seu nome completo')],
        [sg.InputText(key='name')],
        [sg.Text('Email')],
        [sg.InputText(key='gmail')],
        [sg.Text('CPF')],
        [sg.InputText(key='CPF')],
        [sg.Text('Digite sua senha:')],
        [sg.InputText(key='Senha')],
        [sg.Button('Volta'), sg.Button('Cadatrar-se')]
            ]

    window = sg.Window('Cadastro', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == 'Volta':
             window.close()
             Bv()
        if event == 'Cadatrar-se':
            name= values['name']
            gmail=values['gmail']
            CPF=values['CPF']
            Senha=values['Senha']
            if name.isdigit ():
                sg.popup ('Erro: Seu nome é numerico')   
                erros=1
            elif name == '' and gmail == '' and CPF == '' and Senha == '':
                sg.popup("Erro:Não há cadastro salvo")
                erros=1
            elif len(name) <= 3:
                sg.popup('Erro: Nome não é valido')
                erros=1
            elif gmail != '@':
                sg.popup('Erro: Gmail invalido')
                erros=1
            elif not CPF.isdigit():
                sg.popup('Erro: CPF invalido')
                erros=1
            elif not Senha.isdigit():
                sg.popup('Erro: Sua senha so pode ser numerica')
                erros=1
        else:
            window['name'].update(f'')
            window['gmail'].update(f'')
            window['CPF'].update(f'')
            window['Senha'].update(f'')
            sg.popup('cadastro salvo')
            

        window.close()

def Nota():
    aproveitamento = ''
    erro= ""
    lista=[]
    #Notas e nome
    layout = [  [sg.Text("Digite seu Nome: ")],
                [sg.InputText(key='Nome')],
                [sg.Text('Digite a primeira nota:')],
                [sg.InputText(key= 'Nota1')],
                [sg.Text('Digite a segunda nota:')],
                [sg.InputText(key='Nota2')],
                [sg.Button('Finalizar'), sg.Button('Adicionar outro')] ]

    window = sg.Window('Biblioteca de Notas', layout)

    while True:
        event, values = window.read()
       

        if event == sg.WIN_CLOSED:
            break
        if event == "Finalizar":
            if lista  == []:
                sg.popup("Erro: Não ha alunos adicionados")
            else:
                sg.popup(texto)
        if event == 'Adicionar outro':
            Nome= values['Nome']
            Nota1= values['Nota1']
            Nota2= values['Nota2']
            if Nome.isdigit ():
                sg.popup("Erro: digite um nome valido")
                erro = 1
            elif Nome == '' and Nota1 == '' and Nota2 == '':
                sg.popup ('Erro: Os campos estão vazios')
                erro =1
            elif len(Nome) <= 3:
                sg.popup('Erro: o Nome não é valido')
                erro =1
            else:
                window['Nome'].update(f'')
                window['Nota1'].update(f'')
                window['Nota2'].update(f'')
            #Notas
            if Nota1.replace('.', '').isdigit() == True and Nota2.replace('.', '').isdigit() == True:
                Nota1 = float(Nota1)
                Nota2 = float(Nota2)
                Media = (Nota1 + Nota2) / 2
                erro= ''
                if Nota1 <= 10 and Nota2 <= 10:
                    erro=''
            #Media
                    if Media <= 10 and Media >= 9:
                        aproveitamento = "A"
                    elif Media >= 8 and Media <= 8.9:
                        aproveitamento = "B"
                    elif Media >=  7 and Media <= 7.9:
                        aproveitamento = "C"
                    elif Media >= 6 and Media <= 6.9:
                        aproveitamento ="D"
                    elif Media >= 5 and Media <= 5.9:
                        aproveitamento = "E"
                    elif Media <= 5:
                        aproveitamento = "F"
                        print(aproveitamento)     
                    if  Media >= 6:
                        situação= "aprovado"
                    else:
                        situação= "Reprovado"
                else:
                    sg.popup('Erro: digite um numero de 0 a 10')
                    erro =1
            if erro == '':
                lista.append({
            "nome" : Nome,
            "Media" : Media,
            "Situação" : situação,
            "Apro" : aproveitamento
            })
        
            texto = ''
            for i in lista:
                    texto+= (f"Nome:{i['nome']} Media: {i['Media']} Aproveitamento: {i['Apro']} - {i['Situação']},\n")
                    
            print(texto)        
    window.close()

Bv()   