def prettyPrintGrid(g):
    #INPUT: g: a list of lists
    #PROCESS: print it out in rows and columns
    #OUTPUT: none (prints grid)
    for row in g:
        for col in row:
            print(col, end = ' ')
        print()

prettyPrintGrid()