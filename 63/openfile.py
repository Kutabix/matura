def file():
    with open('ciagi.txt', 'r') as file:
        return file.read().splitlines()