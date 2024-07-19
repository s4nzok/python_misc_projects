import string
from random import choice


def create_devices(num_devices = 1, num_subnets = 1):

    created_devices = list()
    # Create empty list for holding devices
    # we can also use: created_devices = []

    if num_devices > 254 or num_subnets >254:
        print("Error: Too many devices/or subnets added!")
        return created_devices

    # For loop to create large number of devices
    for subnets_index in range(1, num_subnets+1):

        for devices_index in range(1, num_devices+1):


            # Create device dictionary
            device = dict()

            # RANDOM DEVICE NAME
            device["name"] = (
                    choice(["r2", "r3", "r4", "r6", "r10"])
                    + choice(['L', 'U'])
                    + choice(string.ascii_letters)
            )
            # RANDOM VENDORS FROM CHOICE OF CISCO, JUNIPER, ARISTA

            device["vendor"] = choice(["Cisco", "Juniper", "Arista"])

            if device["vendor"] == "Cisco":
                device["Os"] = choice(["ios", "ioxe", "ioxr", "nexus"])
                device["version"] = choice(["12.1(T).04", "14.07X.04", "8.12(S).010", "9.1(J).041"])
            elif device["vendor"] == "Juniper":
                device["Os"] = "junos"
                device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
            elif device["vendor"] == "Arista":
                device["Os"] = "eOS"
                device["version"] = choice(["2.45", "2.55", "2.92.145", "3.01"])

            device["ip"] = "10.0." + str(subnets_index) + "." + str(devices_index)

            # ADD THIS DEVICE TO THE LIST OF DEVICES:
            created_devices.append(device)

    return created_devices