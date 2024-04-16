"""
program that pulls out data from an example excel spreadsheet using openpyxl
"""

import openpyxl

workbook = openpyxl.load_workbook('ITEC_Courses.xlsx')

# workbooks (spreadsheets) are composed of sheets
sheet_names = workbook.sheetnames
print(sheet_names)

# assigning variable to the first sheet
codes_sheet = workbook.active  # .active will always be the first

# pulling a specific cell using .value
b2_data = codes_sheet['B2'].value
print(b2_data)

c5_data = codes_sheet['C5'].value
print(c5_data)
print()


# loop that retrieves all data from spreadsheet by row
for row in codes_sheet.rows:
    for cell in row:
        print(cell.value)

print()

# loop that retrieves all data from spreadsheet by columns
for col in codes_sheet.columns:
    for cell in col:
        print(cell.value)

print()


# get all data from one column
class_names_column = codes_sheet['C']  # (could be A, or B for other columns)
for cell in class_names_column:
    print(cell.value)

print()
print('=============== Data from rooms sheet ====================')
print()

# doing same thing as above just with different sheet
rooms_sheet = workbook['rooms']
rooms_column = rooms_sheet['B']
for cell in rooms_column:
    print(cell.value)
