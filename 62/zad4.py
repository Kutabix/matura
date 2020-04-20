from openfile import file

def count6(number):
    return list(str(number)).count('6')

counterDec = 0
counterOct = 0
for n in file('liczby2.txt'):
    counterDec += count6(n)
    counterOct += count6(oct(n))
print(counterDec, counterOct)