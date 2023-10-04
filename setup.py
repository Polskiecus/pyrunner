import getpass
import os, os.path
import sys


app_path = "/home/"+getpass.getuser()+"/.local/bin/pyrunner"
folder_path = "/home/"+getpass.getuser()+"/.local/bin/CustomCommands"
app_code = """#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os, os.path
import getpass


if sys.argv[1] == "-h":
	print("booting into help mode")
	print('''
Avalaible modes:

-h: help mode
-i: information mode
-c: injecting mode
	
Usage: pyrunner [mode]

if you choose injecting mode, 
you need to additionlly
add original filepath and desired command name

ex. pyrunner -c file.py command1''')
	
elif sys.argv[1] == "-i":
	print("Booting into information mode")
	print("Avalaible commands: ")
	
	apps = os.listdir()
	
	for item in apps:
		print(item)
		
elif sys.argv[1] == "-c":
	print("Booted into custom command injecting")
	print("Preparing to inject: "+str(sys.argv[2]))
	
	f = open(sys.argv[2], 'r')
	file_data = f.read()
	f.close()
	
	print("File has been read")
	
	file_data = '''#!/usr/bin/python3
# -*- coding: utf-8 -*-
''' + file_data
	
	print("File has been modified with headers")
	
	new_file_path = '/home/' + getpass.getuser() + '/.local/bin/CustomCommands/' + sys.argv[3]
	print("File path created")
	
	if os.path.isfile(new_file_path):
		
		user_input = ""
		
		while user_input.lower() not in ["n", "y"]:
			user_input = input("There is already a file with that name, do you want to overwrite it?[N/y]\\n")
			
		if user_input.lower() == "n":
			sys.exit()
			
	f = open(new_file_path, "w")
	f.write(file_data)
	f.close()
	
	print("File has been created")
	
	os.system("chmod +x " + new_file_path)
	print("File has been set as a program")
	
else:
	print("Invalid boot mode try using '-h' mode for information")
"""

if os.path.isfile(app_path):

    print("Module is already installed!")
    print("Checking hash")

    f = open(app_path,'r')
    previous_app = f.read()
    f.close()

    previous_hash = hash(previous_app)
    current_hash = hash(app_code)

    print("Previous app hash is: "+str(previous_hash))
    print("Current app hash is:  "+str(current_hash))

    user_input = ""
    while user_input.lower() not in ["n", "y"]:
        user_input = input("Do you want to overwrite the package?[y/n]\n")
        
    if user_input.lower() == 'n':
        sys.exit()


f = open(app_path, 'w')
f.write(app_code)
f.close()
print("File has been written")

os.system("chmod +x " + app_path)
print("File has been set as a program in a path: "+str(app_path))

if '/usr/local/bin' not in os.environ["PATH"].split(":"):
    print("Could not find /usr/local/bin in PATH, you might consider adding it if you want the command to function properly")

if not os.path.isdir(folder_path):
    os.mkdir(folder_path)

if '/usr/local/bin/CustomCommands' not in os.environ["PATH"].split(":"):
    print("Could not find /usr/local/bin/CustomCommands in PATH, you might consider adding it if you want the command to function properly")

print("the setup has ended correctly")
