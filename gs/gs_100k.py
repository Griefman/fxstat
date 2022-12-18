"""
Из данных файла, созданного Индикатором Equity-Monitor,
программа выводит максимальную просадку за день.
"""
import math
name = '61181082_1.csv'

ff = open(name, 'r', encoding='utf-8')
reports = []
for f in ff:
    data = f.strip().split(';')
    if data[2].isalpha():
        pass
    else:
        reports.append([data[0], float(data[2]), float(data[3])])

ff.close()

dct = {}

for i in range(len(reports)):
    if i == len(reports) - 1:
        break
    diff1 = reports[i][2] - reports[i][1]
    diff2 = reports[i+1][2] - reports[i+1][1]
    if reports[i][0] not in dct:
        dct[reports[i][0]] = diff1
    else:
        if diff2 > dct[reports[i][0]]:
            dct[reports[i][0]] = math.ceil(diff2)

print(dct)

dd = 250
count = 0
for k, v in dct.items():
    if v > dd:
        if count > 0:
            print(count * '* ')
        print('CRASH')
        count = 0
    else:
        count += 1
