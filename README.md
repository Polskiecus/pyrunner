# pyrunner
A simple tool for installing python modules as commands inside linux terminal

# Install process
Run a script called setup.py, after that you might need to add some directiores into $PATH,
(if it is going to be required the setup.py will inform you that there are missing path
variables)

# Usage
After the program is successfully installed it creates a dir /usr/local/bin/CustomCommands
in which custom commands can be injected by 

pyrunner -c [original_file_name_to_be_injected] [desired_command_name]

than it can be run just by typing [desired_command_name] directly into the terminal
