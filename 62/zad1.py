from openfile import file

print(oct(min([int(row, 8) for row in [str(n) for n in file('liczby1.txt')]])).split('o')[1])
print(oct(max([int(row, 8) for row in [str(n) for n in file('liczby1.txt')]])).split('o')[1])