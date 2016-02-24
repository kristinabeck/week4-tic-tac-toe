def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
    if board[top-L]==player and board[top-M]==player and board[top-R]==player:
        return 'True'       #across top
    if board[mid-L]==player and board[mid-M]==player and board[mid-R]==player:
        return 'True'       #across middle
    if board[low-L]==player and board[low-M]==player and board[low-R]==player:
        return 'True'       #across bottom
    if board[top-L]==player and board[mid-M]==player and board[low-R]==player:
        return 'True'       #diagonal
    if board[top-R]==player and board[mid-M]==player and board[low-L]==player:
        return 'True'       #diagonal
    if board[top-L]==player and board[mid-L]==player and board[low-L]==player:
        return 'True'       #down the left side
    if board[top-M]==player and board[mid-M]==player and board[low-M]==player:
        return 'True'       #down the middle
    if board[top-R]==player and board[mid-R]==player and board[low-R]==player:
        return 'True'       #down the right side
        
  
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9):
        printBoard(board)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        board[move] = turn
        if( checkWinner(board, 'X') ):  #check if X is winner
            print('X wins!')            #if X winner print X wins   
            break
        elif ( checkWinner(board, 'O') ):   #check if O is winner
            print('O wins!')                #if O winner print O wins
            break
    
        if turn == 'X':                     #players turn
            turn = 'O'
        else:                                   
            turn = 'X'
        
    printBoard(board)
    


    
