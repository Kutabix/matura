from openfile import file

def convertListToInts(list):
    return [int(n) for n in list]

def reverse(number):
    return int(''.join(list(str(number))[::-1]))

howmany = 0
for number in file("liczby.txt"):
    if str(number + reverse(number))[::-1] == str(number + reverse(number)):
        howmany += 1
print(howmany)

