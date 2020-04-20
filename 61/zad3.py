from openfile import file
from statistics import mode
_file = file('bledne.txt')
r = []
for row in _file:
    _r = []
    for i in range(len(row)):
        if i < 5: _r.append(row[i] - row[i-1])
    r.append(mode(_r))
incorrect = []
for i in range(len(_file)):
    for j in range(1, len(_file[i])):
        if _file[i][j] - _file[i][j-1] != r[i] and j == 1:
            if _file[i][j+1]-_file[i][j] == r[i]:
                incorrect.append(_file[i][0])
                break
            else:
                incorrect.append(_file[i][1])
                break
        elif _file[i][j] - _file[i][j-1] != r[i]:
            incorrect.append(_file[i][j])
            break
print(incorrect)