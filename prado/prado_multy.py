import openpyxl

wb = openpyxl.load_workbook('D:\GitHub\/fxstat\prado\jappu_report-28122022.xlsx')
sheet = wb.get_sheet_by_name('Лист1')

print(sheet)
reports = []
for cellObj in sheet['A1': 'N690']:
    report = []
    for cell in cellObj:
        report.append(cell.value)
    if 'cancelled' not in report:
        reports.append(report)

print(reports[0])

# report_dct = {}

pairs_dct = {}
count = 0
for report in reports:
    count += report[-1]
    if report[4] in pairs_dct:
        pairs_dct[report[4]] += report[-1] + float(report[-2]) + float(report[-3]) + float(report[-4])
    else:
        pairs_dct[report[4]] = report[-1] + float(report[-2]) + float(report[-3]) + float(report[-4])

print(count)
for k, v in pairs_dct.items():
    print(k, round(v, 2))
