from openfile import file

def productOfList(number):
    A = [int(row) for row in list(str(number))]
    s = 1
    for n in A:
        s *= n
    return s

def power(number):
    pow = 1
    while len(str(productOfList(number))) > 1:
        pow += 1
        number = productOfList(number)
    return pow

counters = []
maximum = 0
minimum = 0
for i in range(1, 8+1):
    counters.append([power(number) for number in file('liczby.txt')].count(i))
    if minimum == 0 and maximum == 0:
        maximum = max([number for number in file('liczby.txt') if power(number) == 1])
        minimum = min([number for number in file('liczby.txt') if power(number) == 1])
for i in range(len(counters)):
    print((i+1), ' ', counters[i])
print(minimum, maximum)