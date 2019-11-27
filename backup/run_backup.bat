@ECHO OFF
TITLE Backup of Desired Database
COLOR 7C

:BEGIN
    ECHO.
    ECHO "Database Backup Utility"
    ECHO.
    PAUSE
    GOTO BACKUP_DATABASE

:BACKUP_DATABASE
    SET /P M=Enter name of database for backup: 
    SET P=C:\\CEMDAS\Temp\%M%\
    ECHO.
    ECHO "Storing backup to %P%\%M%.bak"
    ECHO "If this is not desired, exit the script now by click the X button or by pressing CTRL+C"
    PAUSE
    MKDIR %P%
    sqlcmd -E -S .\SQLEXPRESS -i "./backup.sql" -v database="%M%" -v filepath="%P%\%M%">> BackupLog.log
    PAUSE