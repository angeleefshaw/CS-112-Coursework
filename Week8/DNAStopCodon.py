def main():
    with open(r'c:\Users\angel\Code\CS-112-Coursework\Week8\dna.txt') as dna:
        dnaString = dna.readlines()
        dna = []
        
        for i in range(len(dnaString)):
            dna.append(dnaString[i].strip('\n'))

        for strand in dna:
            if(strand[-3:] == 'TAA' or strand[-3:] == 'TAG' or strand[-3:] == 'TGA'):
                print(f'{strand} Passes')
            else:
                print(f'{strand} DNA strand has been damaged')

main()