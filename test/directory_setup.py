import sys, os, datetime
path = f'C:\\Users\\{os.getlogin()}\\Desktop\\Generated_Scripts\\' # Location of all generated files. 
try:
    os.mkdir(path)
except FileExistsError as err:
    print(f'Directory {path} already exists. Test Passed.')
    error_log = open('error_log.log', 'a')
    error_log.write('\n------------------------------\n')
    error_log.write(f'{err}\n')
    error_log.write(str(datetime.datetime.now()))