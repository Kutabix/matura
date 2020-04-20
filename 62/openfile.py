def file(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        return [int(row) for row in data]