@ECHO OFF
TITLE Run Tests
COLOR 7C

py directory_setup.py
py db_connect.py
ECHO.
ECHO.
ECHO Das Facts Sheet was generated in the %USERPROFILE%\DESKTOP\Generated_Scripts\databasename Directory. 
PAUSE