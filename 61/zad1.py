from openfile import file

howmany = 0
maxR = 0
for row in file("ciagi.txt"):
    r = []
    for i in range(1, len(row)):
        r.append(row[i]-row[i-1])
    if len(list(dict.fromkeys(r))) == 1:
        howmany += 1
        if list(dict.fromkeys(r))[0] > maxR:
            maxR = list(dict.fromkeys(r))[0]
print(howmany, maxR)