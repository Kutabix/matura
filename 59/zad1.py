from openfile import file

def differentPrimeFactorsLength(number):
    k = 2
    primeFactors = []
    while k * k <= number:
        while number % k == 0:
            if k % 2 == 0:
                return 0
            primeFactors.append(k)
            number /= k
        k += 1
    if number > 1:
        primeFactors.append(int(number))
    return len(list(dict.fromkeys(primeFactors)))

howmany = 0
for number in file("liczby.txt"):
    if differentPrimeFactorsLength(number) == 3:
        howmany += 1
print(howmany)