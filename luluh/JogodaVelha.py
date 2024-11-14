import PySimpleGUI as sg

sg.theme('DarkBlue2')

cont = 0
jogador = 'X'

tabuleiro = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def ler_jogadas(a, b):
    
    #Recebendo o evento
    u = int(a)

    #Criando um tabuleiro invisivel que recebe os dados. O primeiro FOR acessa as linhas.
    for i in range(len(tabuleiro)):
        #O segundo FOR acessa as colunas
        for j in range(len(tabuleiro[i])):
            #Se o valor da coluna acessada for igual a coluna do evento, substituímos o valor numérico atual pelo valor do jogador ('X' ou 'O')
            if tabuleiro[i][j] == u+1 and tabuleiro[i][j] != 'X' and tabuleiro[i][j] != 'O':
                tabuleiro[i][j] = b
                return True
                
def verificar_vencedor():

    # A função verifica linhas, colunas e diagonais
    for i in range(3):
        #O primeiro colchete se refere a linha e o segundo a coluna
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2]:  # Linhas
            Vitória = 'ganhou pelas linhas'
            return Vitória
        elif tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i]:  # Colunas
            Vitória = 'ganhou pelas colunas'
            return Vitória
        
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:  # Diagonal principal
        Vitória = 'ganhou na diagonal principal'
        return Vitória
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:  # Diagonal secundária
        Vitória = 'ganhou na diagonal secundária'
        return Vitória

def verificar_empate():
    
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] in range(1,10):
                return False
    return True

#---------------------------------------------------------------------------------------------------
#Criação da tela

layout = [[sg.Push(), sg.Text('Jogo da Velha'), sg.Push()],
          [sg.Text('')]
          ]

for i in range(3):
    linha = []
    for b in range(3):  
        linha.append(sg.Button('', size=(6, 3), key= str(cont)))
        cont+=1
    layout.append(linha) 

layout.append([
    [sg.Text('')],[sg.Text('', key='-Resultado-')]])

layout.append([sg.Text(f'É a vez do: ({jogador})', key='jogador')])

#---------------------------------------------------------------------------------------------------
#Criação da janela
window = sg.Window('Jogo da Velha', layout, resizable=True)
#---------------------------------------------------------------------------------------------------

while True:
    event, values = window.read()

    # Se o usuário fechar a janela
    if event == sg.WIN_CLOSED:
        break

    if event >= str(0) and event <= str(8):
        #Verifico se a jogada é válida 
        existente = ler_jogadas(event, jogador)
        if existente:
            window[f'{event}'].update(f'{jogador}')
            
            Vitória = verificar_vencedor()
            if Vitória:
                sg.popup(f'O jogador ({jogador}) {Vitória}')
                break
        
            empate = verificar_empate()
            if empate:
                sg.popup(f'A partida terminou em empate')
                break

            #Se (if) for igual a (X) vira (O). Se não (else) vira (X)
            jogador = 'O' if jogador == 'X' else 'X'
            window['jogador'].update(f'É a vez do: ({jogador})')
        else:
            sg.popup('Faça uma jogada válida', title="aaaa")
            
window.close()