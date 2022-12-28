import openpyxl

wb = openpyxl.load_workbook('77-My\Forex\Prado\prado_multy_trades.xlsx')
sheet = wb.get_sheet_by_name('Лист1')

print(sheet)
reports = []
for cellObj in sheet['A1': 'H1053']:
    report = []
    for cell in cellObj:
        report.append(cell.value)


report_dct = {}
print(reports[0])

pairs_dct = {}

for report in reports:
    if report[3] in pairs_dct:
        pairs_dct[report[3]] += report[-1] + float(report[-2]) + float(report[-3])
    else:
        pairs_dct[report[3]] = 0


for k, v in pairs_dct.items():
    print(k, round(v, 2))
