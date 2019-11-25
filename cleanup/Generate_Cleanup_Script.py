# Generates SQL Scripts to perform the final clean up procedures for CEMDAS clients
# !! Use caution when running the SQL scripts and be sure to double check the results !!
import sys
import os

prefix_path = f'C:\\Users\\{os.getlogin()}\\Desktop\\Generated_Scripts\\'

try: # Attempt to create directory. Continues script if directory already exists.
    os.mkdir(f'C:\\Users\\{os.getlogin()}\\Desktop\\Generated_Scripts')
except FileExistsError:
    print(f'Directory {prefix_path} already exists, continuing script.')
    
sys_database_name = input('Enter the name of the Sys1 database, omit the \'Sys1\': \n')
alarm_end_date = input("Enter the data of the first invalid alarm (YYYY-MM-DD): \n")
calibration_end_date = input("Enter the data of the first invalid calibration (YYYY-MM-DD): \n")

script = open(f'{prefix_path}cleanup.sql', 'w+')
script.write(f'USE [{sys_database_name}Sys2]\n')
script.write(f'DELETE FROM ALARMS WHERE TIMESTAMP_OCCUR > \'{alarm_end_date}\';\n')
script.write(f'DELETE FROM CALIBRATION WHERE CAL_TIMESTAMP > \'{calibration_end_date}\';\n')
script.write(f'TRUNCATE TABLE SYS_LOG;\n')
script.write(f'TRUNCATE TABLE ERROR_LOG;\n')
