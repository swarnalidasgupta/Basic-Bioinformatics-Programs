#Computing GC content

with open('dna_sequence.txt', 'r') as file:
    headers = []
    GC_counts_dict = {}
    for line in file:
        new_line = line.strip()
        if new_line.startswith('>'):
            ind_header = new_line.replace('>','')
            headers.append(ind_header)
            GC_count = 0
            total_count = 0
        else:
            total_count += len(new_line)
            GC_count += new_line.count('G') + new_line.count('C')

        GC_content = (GC_count / total_count) * 100 if total_count > 0 else 0
        GC_counts_dict[ind_header] = GC_content

    print(GC_counts_dict)
    max_GC_value = max(GC_counts_dict.items(), key=lambda item: item[1])
    print(max_GC_value)

