from random import choice
from tabulate import tabulate
import string
from operator import itemgetter
from pprint import pprint

devices = list()
# Create empty list for holding devices
# we can also use: devices = []

# For loop to create large number of devices
for index in range(1, 10):

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

    device["ip"] = "10.0.0" + str(index)

    # NICELY FORMATTED PRINT OF THIS ONE DEVICE:
    print()
    for key, value in device.items():
        print(f"{key:>16s}: {value}")

    # ADD THIS DEVICE TO THE LIST OF DEVICES:
    devices.append(device)

# USE PRINT TO PRINT DATA AS IT IS:
print("\n--------DEVICE AS LIST OF DICTS------------------")
pprint(devices)


# USE TABULATE TO PRINT THE TABLE OF THE DEVICES:
print("\n--------SORTED DEVICES IN TABULAR FORM-----------")
print(tabulate(sorted(devices, key=itemgetter('vendor', 'Os', 'version')), headers="keys"))


# WE CAN ALSO PRINT THE TABLE IN THE FOLLOWING WAY:
# sorted_devices = sorted(devices, key=itemgetter('vendor', 'Os', 'version'))
# print(tabulate(sorted_devices, headers="keys"))
 



