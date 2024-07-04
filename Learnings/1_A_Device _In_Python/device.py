from pprint import pprint
device = {'name': 'abcd', 'vendor': 'Cisco', 'model': 'nexus900', 'os': 'nexus', 'version': '9.3(3)', 'ip': '10.1.1.1'}

# simple print
print("\n_____Simple Print______")
print("device:", device)
print("device name:", device["name"])

# pretty print
print("\n_______Pretty Print_______")
pprint(device)

# For loop, nicely formatted print
print("\n________for loop, using fstring________")
for key, value in device.items():
    # for question, answer in device.items():
    # it can also be written like that.
    # item() is going to create a iterable list of dictionary items.
    print(f"{key:>16s} : {value}")
    # : > 16, it is for justifying the string ":"



