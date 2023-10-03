# Organize headers and sequences in a dictionary

with open('rosalind_lcsm.txt', 'r') as input_file:
    header = []
    sequence = []
    for first_sequence in input_file:
        if first_sequence.startswith('>'):
            first_header_trimmed = first_sequence.replace('\n', '')
            header.append(first_header_trimmed)
        else:
            first_sequence_trimmed = first_sequence.replace('\n', '')
            sequence.append(first_sequence_trimmed)

    my_dict = dict(zip(header, sequence))

for value in my_dict.values():
    for char1 in value:
        print(char1)
        
