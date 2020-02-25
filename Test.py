import subprocess # yeah i need that!
import time 
import os
import sys
import platform

# Store current working directory
pwd = os.path.dirname(__file__)
# Append current directory to the python path
sys.path.append(pwd)


win = platform.system() # stores platform name.


print("1. Ubuntu basted os\n")
value = input("Please select os form the list:\n")

if value == "1": 
    print("sudo apt-get update and stuff") # insert data here

elif win == "Windows":
    print("sorry can't run on windows") # windwos erorr
    time.sleep(10) 

else: 
    print(f' {value} is not valid command')
    subprocess.run(["clear"]) 
    subprocess.run(["python3", "Test.py"]) #stupid loop


#LINUX ONLY!!! 

  
