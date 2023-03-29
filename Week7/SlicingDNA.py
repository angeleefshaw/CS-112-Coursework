# Returns a list of codons from a DNA string by storing groups of three letters into a list

dna = "ATGCATTGGAAAAAGATGTGGTAA"
codons = []
start = 0

# Determines the amount of triplets in the dna string
numOfCodons = int(len(dna)/3)

# Append all triplet groups to the codon list
for i in range(numOfCodons):
    triplet = dna[start:start+3]
    codons.append(triplet)
    start = start + 3

print(codons)

