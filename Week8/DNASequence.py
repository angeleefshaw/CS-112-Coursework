dna = "ATGATGTGGTAA"
codons = [ ]
for start in range(0, len(dna), 3):
            print(start)
            triplet = dna[start:start+3]
            codons.append(triplet)
print(codons)

