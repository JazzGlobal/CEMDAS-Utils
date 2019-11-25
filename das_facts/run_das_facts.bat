@ECHO OFF
TITLE Generate Das Facts Sheet
COLOR 7C

py Export_SysParams.py

ECHO.
ECHO.
ECHO Das Facts Sheet was generated in the %USERPROFILE%\DESKTOP\Generated_Scripts\databasename Directory. 
PAUSE