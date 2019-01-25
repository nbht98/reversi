cols = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
rows = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}


def get_opponent(player):
    if player == 'B':
        return 'W'
    else:
        return 'B'


def get_number_choice(value):
    numchoice = ""
    numchoice = numchoice + str(rows[value[1]])
    numchoice = numchoice + str(cols[value[0]])
    return numchoice


def get_char_choice(value):
    charchoice = ""
    for i, j in cols.items():
        if int(j) == int(value[0]):
            charchoice += i
    for i, j in rows.items():
        if int(j) == int(value[1]):
            charchoice += i
    return charchoice


def print_reversi(matrix):
    res = "  a b c d e f g h\n"
    count = 0
    for i in matrix:
        res += str(count + 1) + ' '
        for j in i:
            res = res + j + ' '
        res = res[:-1] + "\n"
        count += 1
    print(res[:-1])


dirlist = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
dirlist.append([-1, -1])


def validPos(x, y):
    return x >= 0 and x < 8 and y >= 0 and y < 8


def canFlip(board, pos, direction, player):
    curX = int(pos[0]) + direction[0]
    curY = int(pos[1]) + direction[1]
    if not validPos(curX, curY):
        return False
    if board[curX][curY] != get_opponent(player):
        return False
    while True:
        (curX, curY) = (curX + direction[0], curY + direction[1])
        if not validPos(curX, curY):
            return False
        if board[curX][curY] == player:
            return True
        if board[curX][curY] == '.':
            return False


def doFlip(board, pos, direction, player):
    board[int(pos[0])][int(pos[1])] = player
    curX = int(pos[0]) + direction[0]
    curY = int(pos[1]) + direction[1]
    while board[curX][curY] == get_opponent(player):
        board[curX][curY] = player
        (curX, curY) = (curX + direction[0], curY + direction[1])


def list_board():
    array = []
    for i in range(8):
        for j in range(8):
            array.append(str(j) + str(i))
    return array


def validMove(board, list_board, player):
    choicelist = []
    for i in list_board:
        for j in dirlist:
            if board[int(i[0])][int(i[1])] == '.':
                if canFlip(board, i, j, player):
                    choicelist.append(get_char_choice(i[::-1]))
    choicelistsort = list(set(choicelist))
    choicelistsort.sort()
    return choicelistsort


def count_points(board):
    points = {}
    countbpoints = 0
    countwpoints = 0
    for i in board:
        countbpoints += i.count('B')
        countwpoints += i.count('W')
    points['B'] = countbpoints
    points['W'] = countwpoints
    return points


def print_ending(board):
    end = count_points(board)
    print("End of the game. ", end="")
    print("W:", end['W'], end="")
    print(", B:", end['B'])
    if end['W'] > end['B']:
        print("W wins.")
    elif end['W'] < end['B']:
        print("B wins.")
    else:
        print("Draw.")


def print_reversi(matrix):
    res = "  a b c d e f g h\n"
    count = 0
    for i in matrix:
        res += str(count + 1) + ' '
        for j in i:
            res = res + j + ' '
        res = res[:-1] + "\n"
        count += 1
    print(res[:-1])


def check_choice(choice, listchoices):
    if choice in listchoices:
        return True
    return False


def newBoard():
    result = []
    for i in range(3):
        result = result + [["."] * 8]
    result = result + [["."] * 3 + ["W", "B"] + ["."] * 3]
    result = result + [["."] * 3 + ["B", "W"] + ["."] * 3]
    for i in range(3):
        result = result + [["."] * 8]
    return result


def checkEndGame(board, list_board, player):
    if len(validMove(board, list_board, player)) == 0:
        if len(validMove(board, list_board, get_opponent(player))) == 0:
            return True
    return False


def stringValidMove(board, list_board, player):
    strValMove = ""
    valMove = validMove(board, list_board, player)
    for i in valMove:
        if i != valMove[len(valMove) - 1]:
            strValMove = strValMove + i + " "
        else:
            strValMove = strValMove + i
    return strValMove


def printToInput(board, list_board, player):
    print_reversi(board)
    if len(validMove(board, list_board, player)) != 0:
        print("Valid choices: ", end='')
        print(stringValidMove(board, list_board, player))
        print("Player", player, end='')
        print(": ", end='')
        inputmove = input()
        while inputmove not in validMove(board, list_board, player):
            print(inputmove, end='')
            print(": Invalid choice")
            print("Valid choices: ", end='')
            print(stringValidMove(board, list_board, player))
            print("Player", player, end='')
            print(": ", end='')
            inputmove = input()
    else:
        inputmove = ""
        print("Player", player, "cannot play.")
    return inputmove


def doMove(board, pos, direction, player):
    for i in direction:
        if canFlip(board, pos, i, player):
            doFlip(board, pos, i, player)
    return board


def playGame():
    board = newBoard()
    listboard = list_board()
    player = 'B'
    while checkEndGame(board, listboard, player) is False:
        move = printToInput(board, listboard, player)
        if move != "":
            board = doMove(board, get_number_choice(move), dirlist, player)
        player = get_opponent(player)
    move = printToInput(board, listboard, player)
    move = printToInput(board, listboard, get_opponent(player))
    print_ending(board)


playGame()
