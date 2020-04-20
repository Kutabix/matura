from openfile import file

cubes = []
for i in range(1, 101):
    cubes.append(i**3)

for row in file('ciagi.txt'):
    max = 0
    for item in row:
        if item in cubes and item > max:
            max = item
    if max != 0:
        print(max)