import pyeapi
import yaml

pyeapi.load_config("eapi.conf")                         #Load the switch credentials for login

file = open("vlans.yml", "r")                           #Load the vlans.yml file
vlan_dict = yaml.safe_load(file)                        #Store the contents of vlans.yml into a dictionary


for switch in vlan_dict["switches"]:                    #Iterate through each switch in vlans.yml
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)                 #Connect to the switch
    vlan_api = connect.api("vlans")                     #API call for editing the VLANs
    for vlan in vlan_dict["vlans"]:                     #Iterate through each VLAN in vlans.yml
        vlan_id = vlan["id"]                            #Store the VLAN ID
        vlan_name = vlan["name"]                        #Store the VLAN name
        print(f"Adding VLAN {vlan_id} to {switch}")
        vlan_api.create(vlan_id)                        #Create the VLAN
        vlan_api.set_name(vlan_id, vlan_name)           #Add the VLAN name