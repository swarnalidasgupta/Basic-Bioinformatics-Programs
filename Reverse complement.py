# Practice 3

with open('dna_sequence.txt', 'r') as input_file:
    reverse_complement = ''
    for lines in input_file:
        reverse_dna = ''.join(reversed(lines))
        for rna in reverse_dna:
            if rna == 'T':
                reverse_complement += 'A'
            elif rna == 'G':
                reverse_complement += 'C'
            elif rna == 'A':
                reverse_complement += 'T'
            elif rna == 'C':
                reverse_complement += 'G'
        print(reverse_complement)



