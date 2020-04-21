from openfile import file

def primeFactiorization(number):
    k = 2
    factors = 0
    while k*k <= number:
        while number % k == 0:
            number /= k
            factors += 1
            if factors > 2:
                return factors
        k += 1
    if number > 1:
        factors += 1
    return factors

howmany = 0
min = max([int(binary, 2) for binary in file()])
max = 0
for binary in file():
    if primeFactiorization(int(binary, 2)) == 2:
        howmany += 1
        if int(binary, 2) > max:
            max = int(binary, 2)
        if int(binary, 2) < min:
            min = int(binary, 2)
print(howmany, min, max)