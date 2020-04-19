def file():
    file = open('liczby.txt', 'r')
    data = file.readlines()
    return [int(number) for number in data]

