import random
player1Number = 0
player2Number = 0
player1Point = 0
player2Point = 0
tryAgain = "yes"
while tryAgain == 'yes':
    diceNumber = random.randint(1, 100)
    player1Number = int(input('Player 1, Input a number 1-100: '))
    for i in range(50):
        print(' ')
    player2Number = int(input('Player 2, Input a number 1-100: '))
    print('The number was', diceNumber)
    newPlayer1Number = abs(diceNumber - player1Number)
    newPlayer2Number = abs(diceNumber - player2Number)
    if newPlayer1Number < newPlayer2Number:
        print('Player 1 Wins!')
        player1Point += 1
    elif newPlayer1Number > newPlayer2Number:
        print('Player 2 Wins!')
        player2Point += 1
    else:
        print("Tie!")
        
    tryAgain = input('Do you want to try again? yes or no: ').lower()
