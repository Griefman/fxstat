

name = r'''61181082_1.csv'''

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
            dct[reports[i][0]] = round(diff2, 2)

print(dct)
