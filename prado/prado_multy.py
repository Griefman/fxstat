import openpyxl

wb = openpyxl.load_workbook('Y:\YandexDisk\GitHub\/fxstat\prado\prado_multy_trades_do-28022024.xlsx')
sheet = wb.get_sheet_by_name('Лист1')

print(sheet)
reports = []
for cellObj in sheet['A3': 'I2279']:
    report = []
    for cell in cellObj:
        report.append(cell.value)
    if 'cancelled' not in report and ('usdjpy' in report or 'cadjpy' in report or 'xauusd' in report):
        reports.append(report)

# print(reports[:-10])
print(len(reports))

# Получить список дат в формате 2022.01


def get_dates(reps):
    dates = []
    for rep in reps:
        date = rep[0][0:7]
        dates.append(date)
    lst = list(set(dates))
    lst.sort()
    return lst


dates_lst = get_dates(reports)
print(dates_lst)


def get_month_report(month, reports):
    month_reports = []
    for rep in reports:
        if month in rep[0]:
            month_reports.append(rep)
    return month_reports


print(get_month_report('2022.10', reports))


pairs_dct = {}
count = 0
for report in reports:
    profit = float(report[-1]) + float(report[-2]) + float(report[-3]) + float(report[-4])
    count += profit
    if report[2] in pairs_dct:
        pairs_dct[report[2]] += profit
    else:
        pairs_dct[report[2]] = profit

print(count)
for k, v in pairs_dct.items():
    print(k, round(v, 2))
