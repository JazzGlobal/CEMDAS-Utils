# Generates SQL Scripts to perform the final clean up procedures for CEMDAS clients
# !! Use caution when running the SQL scripts and be sure to double check the results !!
import sys, os, datetime
prefix_path = f'C:\\Users\\{os.getlogin()}\\Desktop\\Generated_Scripts\\'

try: # Attempt to create directory. Continues script if directory already exists.
    os.mkdir(f'C:\\Users\\{os.getlogin()}\\Desktop\\Generated_Scripts')
except FileExistsError:
    print(f'Directory {prefix_path} already exists, continuing script.')

sys_database_name = input('Enter the name of the Sys1 database, omit the \'Sys2\': \n')
alarm_end_date = input("Enter the data of the first invalid alarm (YYYY-MM-DD): \n")
calibration_end_date = input("Enter the data of the first invalid calibration (YYYY-MM-DD): \n")

# Store into a string for usage in multiple locations.
sql_string = ""
sql_string+= f'USE [{sys_database_name}Sys2]\n'
sql_string+= f'DELETE FROM ALARMS WHERE TIMESTAMP_OCCUR > \'{alarm_end_date}\';\n'
sql_string+= f'DELETE FROM CALIBRATION WHERE CAL_TIMESTAMP > \'{calibration_end_date}\';\n'
sql_string+= f'TRUNCATE TABLE SYS_LOG;\n'
sql_string+= f'TRUNCATE TABLE ERROR_LOG;\n'

# Write to SQL Script

try: # Attempt to create directory. Continues script if directory already exists.
    os.mkdir(f'{prefix_path}{sys_database_name}')
except: 
    print(f'Directory {prefix_path} already exists, continuing script.')

script = open(f'{prefix_path}\\{sys_database_name}\\cleanup.sql', 'w+')
script.write(f'{sql_string}')

# Write to Application Log file.
log = open(f'{prefix_path}{sys_database_name}\\cleaup_log.log', 'a')
log.write('--------------------\n')
log.write(f'Wrote to SQL Script on {str(datetime.datetime.now())}\n')
log.write('====================\n')
log.write(f'{sql_string}\n')
log.write('--------------------\n')
