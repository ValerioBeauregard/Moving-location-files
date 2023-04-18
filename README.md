# Moving location files Python Script

This little code writen in python takes all the files with the given string starting, and move it to another folder location.

## Considerations
1. In line 6, you have to specify the new location for the files.

2. In line 9:
```
escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
```
You have to replace "Desktop" with the name of the folder where you want to look up to move the files.

3. In line 12, you have to replace "Captura de Pantalla" with the inicial string that the program will use to find out the files you want to move.
