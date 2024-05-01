player1 = float(input('Bienvenido al juego eres el player 1 para seleccionar piedra marca 1, para selcionar papel marca 2, para selecionar tijera marca 3 '))
player2 = float(input('Eres el player 2 para seleccionar piedra marca 1, para selcionar papel marca 2, para selecionar tijera marca 3 '))


if player1 == player2:
    print("empate")
elif player1 ==1: 
    if player2 ==2:
        print( "player 2 gana")
    elif player2 == 3:
        print("player 1 gana")
    else:
        print("player 2 comando no valido")
elif player1 ==2:
    if player2 ==1:
       print("player 2 gana")
    elif player2 == 2:
        print("player 1 gana")
    else:
        print("player 2 comando no valido")
elif player1 ==3:
    if player2 ==1:
       print("player 2 gana")
    elif player2 == 2:
        print("player 1 gana")
    else:
        print("player 2 comando no valido")
else:
    print('player 1 comando no valido')












