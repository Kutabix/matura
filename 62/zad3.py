from openfile import file

a = 0
b = 0
for i in range(1000):
    if int(str(file('liczby1.txt')[i]), 8) == file('liczby2.txt')[i]:
        a += 1
    elif int(str(file('liczby1.txt')[i]), 8) > file('liczby2.txt')[i]:
        b += 1
print(a, b)