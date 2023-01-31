# V = R-2ES is the formula used to determine
# the amount of vines that will fit into any given
# vineyard row

rowLength = input("What is the length of the row? ")
endPostLength = input('What is the amount of spance used by an end-post assembly? ')
vineSpace = input('How much space would you like between each vine? ')

v = (int(rowLength) - (2*int(endPostLength)*int(vineSpace)))

if v > 0:
    print(f'You will be able to plant {v} vines')
else:
    print('There is not sufficient space in the row to plant any vines')