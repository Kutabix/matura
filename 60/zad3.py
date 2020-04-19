from math import gcd
from openfile import file

max = 0
for i in range(len(file())):
    if all(gcd(file()[i], number) == 1 for number in file()[0:i] + file()[i+1:len(file())]):
        if file()[i] > max:
            max = file()[i]
print(max)