from openfile import file

def divisions(number):
    divisions = 2
    i = 2
    divisionList = [1, number]
    while i*i <= number:
        if number % i == 0 and number/i != i:
            divisions += 2
            divisionList.append(int(number/i))
            divisionList.append(i)
        if number / i == i:
            divisionList.append(i)
            divisions += 1
        i += 1
    return [divisions, sorted(divisionList)]

for number in file():
    if divisions(number)[0] == 18:
        print(number, divisions(number)[1])
