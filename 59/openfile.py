def file(filename):
    with open(filename, "r") as file:
        data = file.readlines()
        return [int(row) for row in data]
