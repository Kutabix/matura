from openfile import openfile

s1 = openfile("dane_systemy1.txt")
s2 = openfile("dane_systemy2.txt")
s3 = openfile("dane_systemy3.txt")

howmany = 0
for i in range(1095):
    if int(s1[i][0], 2) != 12 + 24 * i and int(s2[i][0], 4) != 12 + 24 * i and int(s3[i][0], 8) != 12 + 24 * i:
        howmany += 1
print(howmany)