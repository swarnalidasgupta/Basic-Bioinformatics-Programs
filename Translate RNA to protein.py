# RNA to protein

codon_dictionary = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V', 'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
                    'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V', 'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
                    'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
                    'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
                    'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
                    'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
                    'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
                    'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
                    'UAA':'Stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
                    'UAG':'Stop', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
                    'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
                    'UGC':'C',  'CGC':'R', 'AGC':'S', 'GGC':'G',
                    'UGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',
                    'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'
                    }


with open('rna_sequence.txt', 'r') as rna_seq:
    pro_chain = ''
    for line in rna_seq:
        # The line is stored in a string
        edited_line = line.replace('\n', '')
        # The range must include length of entire rna sequence, otherwise it won't go till the end!
        for i in range(0, len(edited_line), 3):   # Increment by 3
            codon = edited_line[i:i+3]  # String slicing
            if codon in codon_dictionary.keys():
                pro_seq = codon_dictionary[codon]
                pro_chain += pro_seq
print(pro_chain)

