#Calculate hamming distance in two DNA sequences

with open('dna_sequence.txt', 'r') as dna_file:
    lines = []
    for line in dna_file:
        edited_line = line.strip()
        lines.append(edited_line)
    print(lines)
    hamming_counter = 0
    for char1, char2 in zip(lines[0], lines[1]):
        if char1 != char2:
            hamming_counter += 1
    print(hamming_counter)

