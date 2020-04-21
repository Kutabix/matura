from openfile import file

howmany = 0
for binary in file():
    if binary.find('11') == -1:
        howmany += 1
print(howmany)