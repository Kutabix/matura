from openfile import file

for binary in file():
    if len(binary) % 2 == 0 and binary[:int(len(binary)/2)] == binary[int(len(binary)/2):]:
        print(binary)
