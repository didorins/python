# Simple program to open a file and append string to file contents. Used while loop to do number of iterations and then read the file in the end.

# Open and write to file. Second arguemnt of open should be 'w' to overwrite or 'a' to add.. Functions in write must be strings, hence strftime in timenow var.
# Import builtin function time and combine with sleep arguement 
# While loop to iterate 10 times, starting from 0 and add +1 to var i on each iteration
from datetime import datetime
import time

# in write mode delete contents, so we can append on top of clear file later
with open("stuff.txt", "w") as deletefile:
    deletefile.write("")

i = 0
while i < 10:
    timenow = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    with open("stuff.txt", "a") as writefile:
        writefile.write("The date and time is " + timenow + '\n')
        time.sleep(1)
        i += 1
# Open file with context manger 'with'. Note that cursor moves in the end, so save constant in variable to repeat

with open("stuff.txt") as myyfile:
    contentt = myyfile.read()   
print(contentt) 

