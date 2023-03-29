def main():
    board = [['*','*','*'],['*','*','*'],['*','*','*']]
    #board2 = [['O','X','O'],['X','X','O'],['X','O','X']] #full, no winner
    #board3 = [['X','*','O'],['*','O','X'],['O','*','*']] #not full, winner
    print(isWinner(board))
    print(isFull(board))

    board[1][1] = "X"
    prettyPrintGrid(board)
    prettyPrintComplicated(board)

def prettyPrintGrid(g):
    #INPUT: g: a list of lists
    #PROCESS: print it out in rows and columns
    #OUTPUT: none (prints grid)
    for row in g:
        for col in row:
            print(col, end = ' ')
        print()

def prettyPrintComplicated(g):
    #INPUT: g: a 3 x 3 list of lists
    #PROCESS: print it out like a TTT board
    #OUTPUT: none (prints grid)

    for r in range(len(g)):
        row = g[r]  # next row
        for c in range(len(row)):
            if c ==0:
                print(row[c],end="")
            else:
                print("|"+row[c], end="")
        # go to next row with spacer between middle rows
        if r < 2:
            print("\n-+-+-",end="") 
        print()
        


def isFull(b):
    for row in b:
        if "*" in row:
            return(False)
    return(True)
    
def isWinner(b):
    #input: board (b) initialized with * in the blank cells
    #output: True if there is a winner, False if not
    #action: checks for all possible ways of winning

    winner = False
    #win by rows (check each row) 
    for r in range(3):
        if( b[r][0] != '*') and (b[r][0] == b[r][1] == b[r][2]):
                winner = True
    #win by columns (check each column)
    for c in range(3):
        if( b[0][c] != '*')and (b[0][c] == b[1][c]  == b[2][c]):
                winner = True        
    #win by diagonals 
    if( b[1][1] != '*'):
        if (b[0][0] == b[1][1] == b[2][2]):
            winner = True
        elif (b[0][2] == b[1][1] == b[2][0]):
            winner = True
    return(winner) 


main()
