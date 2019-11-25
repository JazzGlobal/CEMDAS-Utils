# Test Script to verify database connection.
import sys, os, pymssql, datetime

database_name = input('Enter the name of the Sys1 database (Without Sys1): ')

# Database Connection Configuration
try:
    connection = pymssql.connect(
                    server=f"{os.getlogin()}\\SQLEXPRESS",
                    port=1433,
                    user="sa",
                    password="sa123",
                    database=(f'{database_name}Sys1'))
except Exception as err: 
    error_log = open('error_log.log', 'a')
    error_log.write('\n------------------------------\n')
    error_log.write(f'{err}\n')
    error_log.write('Could not connect to SQL Server.\n')
    error_log.write(str(datetime.datetime.now()))
