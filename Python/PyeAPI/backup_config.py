import pyeapi
import os
import yaml

pyeapi.load_config("eapi.conf")                             #Load the switch credentials for login

file = open("switches.yml", "r")                            #Load the switches.yml file
switch_dict = yaml.safe_load(file)                          #Store the contents of switches.yml into a dictionary

directory = "configs"                                       #Check if the directory "configs" exists, if not create the directory
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

for switch in switch_dict["switches"]:                      #Iterate through each switch
    connect = pyeapi.connect_to(switch)                     #Connecting to the switch
    running_config = connect.get_config(as_string=True)     #API call to get running config
    path = directory+"/"+switch+".cgf"                      
    print(f"Backing up {switch}")
    file = open(path, "w")                                  #Create the file to write the backup to
    file.write(running_config)                              #Write the backup to the file
    file.close()
    print(f"{switch} backup complete")