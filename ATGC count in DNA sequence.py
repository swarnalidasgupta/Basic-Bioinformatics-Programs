A_count = 0
C_count = 0
G_count = 0
T_count = 0

with open('dna_sequence.txt', 'r') as file:
    for line in file:
        for letter in line:
            if letter == 'A':
                A_count += 1
            elif letter == 'C':
                C_count += 1
            elif letter == 'G':
                G_count += 1
            elif letter == 'T':
                T_count += 1

    print(f'{A_count} {C_count} {G_count} {T_count}')

