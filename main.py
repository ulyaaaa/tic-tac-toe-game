board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
  print('-------------')
  print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
  print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
  print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
  print('-------------')
    
def isWinner(we, le):
    return (we[7] == le and we[8] == le and we[9] == le) or (we[4] == le and we[5] == le and we[6] == le) or(we[1] == le and we[2] == le and we[3] == le) or(we[1] == le and we[4] == le and we[7] == le) or(we[2] == le and we[5] == le and we[8] == le) or(we[3] == le and we[6] == le and we[9] == le) or(we[1] == le and we[5] == le and we[9] == le) or(we[3] == le and we[5] == le and we[7] == le)
  
def playerMove():
    run = True
    while run:
        move = input('Select a position (1-9) >') 
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('the space is filled!')
            else:
                print('please type a number 1-9!')
        except:
            print('type a number!')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def minimax(pos, node, depth, player):
        if depth == 0 or node.gameOver():
            if node.checkWin() == "X":
                return 0
            elif node.checkWin() == "O":
                return 100
            else:
                return 50

        if player == "O":
            bestValue = 0
            for move in node.availableMoves():
                node.makeMove(move, player)
                moveValue =pos.minimax(node, depth-1, (player))
                node.makeMove(move, " ")
                bestValue = max(bestValue, moveValue)
            return bestValue
        
        if player == "X":
            bestValue = 100
            for move in node.availableMoves():
                node.makeMove(move, player)
                moveValue = pos.minimax(node, depth-1, (player))
                node.makeMove(move, " ")
                bestValue = min(bestValue, moveValue)
            return bestValue

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('O\ is WIN!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie!')
            else:
                insertLetter('O', move)
                print('Computer placed in position', move , ':')
                printBoard(board)
        else:
            print('YOU\ WIN!')
            break

    if isBoardFull(board):
        print('Tie!')

while True:
    answer = input('play the game?') 
    if answer.lower() == 'y' or answer.lower == 'yes':
        main()
    else:
        break

while True:
  answer = input('play the game?')
  if answer.lower() == 'n' or answer.lower == 'no':
    print('see u again')
  else:
    break
    
    