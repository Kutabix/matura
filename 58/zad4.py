from openfile import openfile

s1 = openfile("dane_systemy1.txt")

dec = [int(row[1], 2) for row in s1]

max = 0

for i in range(len(dec)):
    for j in range(i+1, len(dec)):
        if (pow(dec[i]-dec[j], 2)/abs(i-j)) > max:
            max = (pow(dec[i]-dec[j], 2)/abs(i-j))
print(round(max) + 1)