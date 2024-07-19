

from Util.Create_Utils import create_devices

# We use . to specify directories.
# Here we are importing a utils module from the python package named "Util"

from tabulate import tabulate

# importing the function from the module("Create_Utils.py")
# if you want to import whole module than the one function:
# you can do: 0r u can use: "util." as:
# devices = util.create_devices(num_devices=4, num_subnets=5)

# ---MAIN PROGRAM----------------__________________

if __name__ == '__main__':

    devices = create_devices(num_devices=4, num_subnets=5)
    print("\n", tabulate(devices, headers="keys"))