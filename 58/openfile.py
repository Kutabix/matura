def openfile(filename):
    result = []
    with open(filename) as file:
        result = [[row.split(' ')[0], row.split(' ')[1].split('\n')[0]] for row in file]
    return result

