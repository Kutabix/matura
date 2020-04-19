from openfile import file

penult = file()[0]
last = file()[1]
howmany = 0

for i in range(2, len(file())):
    if file()[i] < 1000:
        penult = last
        last = file()[i]
        howmany += 1
print(howmany, penult, last)

