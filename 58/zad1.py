from openfile import openfile

decs_1 = min([int(row[1], 2) for row in openfile("dane_systemy1.txt")])
decs_2 = min([int(row[1], 4) for row in openfile("dane_systemy2.txt")])
decs_3 = min([int(row[1], 8) for row in openfile("dane_systemy3.txt")])


print('-' + bin(decs_1).split('-0b')[1])
print('-' + bin(decs_2).split('-0b')[1])
print('-' + bin(decs_3).split('-0b')[1])