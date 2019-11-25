# Queries the SYS_PARAMS table of a specified database
# Exports the results to a spreadsheet to generate the DasFactsSheet

import sys, os, openpyxl, pymssql
from openpyxl.utils import get_column_letter

database_name = input('Enter the name of the Sys1 database (Without Sys1)')

# Database Connection Configuration
connection = pymssql.connect(
                server=f"{os.getlogin()}\\SQLEXPRESS",
                port=1433,
                user="sa",
                password="sa123",
                database=(f'{database_name}Sys1'))

# File Location Configuration. 
prefix_path = f'C:\\Users\\{os.getlogin()}\\Desktop\\Generated_Scripts\\' # Location of all generated files. 

try: # Attempt to create directory. Continues script if directory already exists.
    os.mkdir(prefix_path)
except FileExistsError:
    print(f'{prefix_path} already exists, continuing script.')

workbook_path = f'{prefix_path}template_DasFacts.xlsx' # Path of workbook template. 
work_book = openpyxl.load_workbook(workbook_path)
sheet = work_book['Sheet1']
cursor = connection.cursor()

def GetSystemParameters():
    cursor.execute('SELECT * FROM SYS_PARAMS')
    sqlData = []
    for row in cursor.fetchall():  
        dataRow = { 
            # Adding the correct SQL Database field into our dictionary. 
            # FORMAT:
            # Key in the dictionary: SQL Database Column data.
            "param_index": row[0],
            "param_name": row[1],
            "site": row[2],
            "calc_id": row[13],
            "lower_limit_cu": row[23],
            "upper_limit_cu": row[24],
            "lower_limit_eu": row[25],
            "upper_limit_eu": row[26],
            "unit_conversion": row[39],
            "data_source": row[40],
        }
        sqlData.append(dataRow)
    return sqlData

# Create Sys_Param List
toExport = GetSystemParameters()

# Iterate through Sys_Params list.
for parameter in range(len(toExport)):
    for db_field in range(len(toExport[parameter])):
        column_letter = get_column_letter(db_field+1)
        sheet[f'{column_letter}{parameter+2}'] = list(toExport[parameter].values())[db_field] # We use x+2 as the index to start AFTER Row 1. 

work_book.save(f'{prefix_path}{database_name}DasFacts.xlsx')
connection.close()