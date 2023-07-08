def sliceDNA(dna):
    codons = []
    start = 0

    numOfCodons = int(len(dna)/3)

    # Append all triplet groups to the codon list
    for i in range(numOfCodons):
        triplet = dna[start:start+3]
        codons.append(triplet)
        start = start + 3

    return(codons)
