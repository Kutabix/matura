def convertListToIntegers(list):
    return [int(item) for item in list]

def file(filename):
    with open(filename) as txtFile:
        list = [line.split() for line in txtFile]
        return [convertListToIntegers(row) for row in list[1:len(list):2]]
