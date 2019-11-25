USE [$(database)]
BACKUP DATABASE [$(database)]
TO DISK = '$(filepath)'