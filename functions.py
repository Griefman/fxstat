import csv
import openpyxl


def get_data_from_xlsx(file_name, list_name, start_cell, end_cell):
    wb = openpyxl.load_workbook(file_name)
    sheet = wb.get_sheet_by_name(list_name)
    reports = []
    for cellObj in sheet[start_cell: end_cell]:
        report = []
        for cell in cellObj:
            report.append(cell.value)
    return reports


def get_data_from_csv(file_name):
    reports = []
    with open(file_name, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            reports.append(row)
    return reports


