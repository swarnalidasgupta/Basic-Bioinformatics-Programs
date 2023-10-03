# Count open reading frames in the RNA

with open('rosalind_subs.txt', 'r') as string_file:
    my_list = []
    for code in string_file:
        edited_code = code.replace('\n', '')
        my_list.append(edited_code)

seq = my_list[0]
query = my_list[1]
n = len(query)
m = len(seq)
index_list = []
counter = 0

for i in range(counter, m):
    ref_seq = seq[i:i+n]
    if ref_seq == query:
        index_list.append(i)
    counter += 1
print(index_list)

for i in range(0, len(index_list)):
    index_list[i] += 1
print(index_list)
