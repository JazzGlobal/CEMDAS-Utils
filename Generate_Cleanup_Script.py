# Generates SQL Scripts to perform the final clean up procedures for CEMDAS clients
# !!Use caution when running the SQL scripts and be sure to double check the results!!
import sys
import os
try:
    os.mkdir(f'C:\\Users\\{os.getlogin()}\\Desktop\\Generated_Scripts')
except FileExistsError:
    print('Directory already exists')

path = f'C:\\Users\\{os.getlogin()}\\Desktop\\Generated_Scripts\\cleanup.sql'
alarmEndDate = input("Enter the data of the first invalid alarm: ")
calibrationEndDate = input("Enter the data of the first invalid calibration: ")
opLogEndDate = input("Enter the data of the first invalid op_log entry: ")



script = open(path, 'w+')
script.write(f'DELETE FROM ALARMS WHERE TIMESTAMP_OCCUR > \'{alarmEndDate}\';\n')
script.write(f'DELETE FROM CALIBRATION WHERE CAL_TIMESTAMP > \'{calibrationEndDate}\';\n')
script.write(f'DELETE FROM OP_LOG WHERE TIMESTAMP > \'{opLogEndDate}\';\n')
script.write(f'TRUNCATE TABLE SYS_LOG;\n')
script.write(f'TRUNCATE TABLE ERROR_LOG;\n')
