import sys
def createGame(inpt=3):
    #    game= [[0] * inpt] * inpt
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    return game


def placeonboardGame(game, location: tuple, player: int):
    x, y = location
    game[int(x)][int(y)] = player


def checkWinner(game):
    for row in range(len(game)):
        if game[row][0] == game[row][1] == game[row][2] and game[row][0] != 0:
            print("Player " + str(row[0]) + " has won, unlucky \n")
            return True
    for column in range(len(game)):
        if game[0][column] == game[1][column] == game[2][column] and game[0][column] != 0:
            print("Player :" + str(game[0][column]) + " has won, unlucky \n")
            return True
    for diagonal in range(len(game)):
        if (game[0][0] == game[1][1] == game[2][2] and game[0][0] != 0) or (
                game[2][0] == game[1][1] == game[0][2] and game[2][0] != 0):
            print("Player :" + str(game[1][1]) + " has won, unlucky \n")
            return True

    print("nobody won yet")
    return False


def turnOf(player, game):
    print("Player " + str(player) + " Turn: \n")
    while True:
        inpt = tuple(input("Where would you like to place?").split())
        if len(inpt) != 2:
            print("invalid values given")
            continue
        if game[int(inpt[0])][int(inpt[1])] == 0:
            placeonboardGame(game, inpt, player)
            break
        elif game[int(inpt[0])][int(inpt[1])] == player:
            print("you already marked there")
            continue
        else:
            print("Your opponent placed his marker there")
            continue
    if player == 1:
        return 2
    else:
        return 1


def drawBoard(game):
    for row in game:
        print(" --- " * len(row))
        for column in row:
            if column == 1:
                drawable = " X "
            elif column == 2:
                drawable = " O "
            else:
                drawable = "   "
            print("|" + drawable + "|", end="")
        print()
    print(" --- " * len(game[0]))


def TickTackToeRun():
    counter = 0
    game = createGame()
    print("""

    Welome to the tickTackToe GAME

    """)

    # 1= x , 2= o , 0= AF EHAD Rik
    while True:
        counter += 1
        currentPlayer = 1
        print("""
        Round """ + str(counter) + "\n"
              )
        print(""" 

        The board is of the following:

         """)
        drawBoard(game)
        print("\n")
        currentPlayer = turnOf(currentPlayer, game)
        if (checkWinner(game)):
            print("GAME OVER")
            break
        print(""" 

        The board is of the following:

         """)
        drawBoard(game)
        currentPlayer = turnOf(currentPlayer, game)
        if (checkWinner(game)):
            print("GAME OVER")
            break

    sys.exit()
