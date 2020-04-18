data_file = open("dane4.txt", 'r')
data = data_file.read().splitlines()

gaps = []

for i in range(1, len(data)):
    gaps.append(abs(int(data[i]) - int(data[i-1])))

non_duplicates_gaps = list(dict.fromkeys(gaps))

max_occurences = 0
two_last = []

for i in range(len(non_duplicates_gaps)):
    if gaps.count(non_duplicates_gaps[i]) >= max_occurences:
        max_occurences = gaps.count(non_duplicates_gaps[i])
        two_last.append(non_duplicates_gaps[i])
