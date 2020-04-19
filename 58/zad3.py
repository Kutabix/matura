from openfile import openfile

s1 = openfile("dane_systemy1.txt")
s2 = openfile("dane_systemy2.txt")
s3 = openfile("dane_systemy3.txt")

# function that returns sublist of list <system> from index 0 to <end-1> also converted from <s> to dec system
def sl(system, end, s):
    return [int(row[1], s) for row in system[0:end]]

# function that returns <list> converted from <system> to decimal
def clts(list, system):
    return [int(row, system) for row in list]

howmany = 1
for i in range(1, 1095):
    if int(s1[i][1], 2) > max(sl(s1, i, 2)) or int(s2[i][1], 4) > max(sl(s2, i, 4)) or int(s3[i][1], 8) > max(sl(s3, i, 8)):
        howmany += 1
print(howmany)