import paramiko

# Cisco device details
DEVICE_IP = '192.168.1.1'      # Replace with your device's IP address
USERNAME = 'sanzok'     # Replace with your SSH username
PASSWORD = 1234     # Replace with your SSH password

# Commands to be executed on the Cisco device
CONFIG_COMMANDS = [
    'hostname MyRouter',
    'username admin privilege 15 secret cisco123',
    'line con 0',
    'login local',
    'exit',
    'line vty 0 4',
    'login local',
    'exit',
    'end',
    'write memory'
]

def send_commands_over_ssh(ip, user, passwd, commands):
    """Connect to a Cisco device via SSH and send commands."""
    try:
        # Create SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device
        client.connect(ip, username=user, password=passwd)

        # Open an interactive shell
        shell = client.invoke_shell()
        shell.settimeout(10)

        # Send each command from the command list
        for command in commands:
            shell.send(command + '\n')
            time.sleep(1)  # Wait for the command to be processed

        # Close the connection
        client.close()
        print("Commands sent successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    send_commands_over_ssh(DEVICE_IP, USERNAME, PASSWORD, CONFIG_COMMANDS)
