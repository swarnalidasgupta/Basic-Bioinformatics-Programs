# Convert DNA to RNA (Transcribe DNA sequence)

with open('dna_sequence.txt', 'r') as dna_file:
    new_rna = ''
    for dna in dna_file:
        #The for loop stores the line read in a string
        for nucleotide in dna:
            if nucleotide == 'T':
                new_rna = dna.replace('T', 'U')
            else:
                continue
    print(new_rna)

