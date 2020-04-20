from openfile import file

f = file('liczby2.txt')
length = 1
first = 0
maxLength = 0
for i in range(1, len(f)):
    if f[i] >= f[i-1]:
        length += 1
        if i == len(f) - 1 and length > maxLength:
            maxLength = length
    else:
        if length != 1 and length > maxLength:
            maxLength = length
            first = f[i - length]
        length = 1

print(first, maxLength)
