import subprocess
import click
from pick import pick
from getpass import getpass

def split_with_escaping(string, separator, escape="\\"):
    is_escaped = False
    parts = [""]

    for char in string:
        if char == separator and not is_escaped:
            parts.append("")

        elif char == escape:
            if not is_escaped:
                is_escaped = True
            else:
                is_escaped = False
                parts[-1] += char
        else:
            parts[-1] += char
            is_escaped = False

    return parts[:-1]

@click.group()
def cli(): pass

@cli.command()
def connect():
    print("Loading wifi networks...")

    proc = subprocess.Popen(["nmcli", "-t", "dev", "wifi", "list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.wait():
        print(proc.stderr.read())
        exit(proc.returncode)

    wifi_list_raw = proc.stdout.read().decode()

    wifi_list = [
            split_with_escaping(network, ":")
            for network in
            wifi_list_raw.split("\n")
    ][:-1]

    selection = [i[2] + " " + i[7] for i in wifi_list]
    selected = pick(selection, "WiFi networks:")[1]
    
    ssid = wifi_list[selected][2]

    password = getpass()

    prompt = ["nmcli", "dev", "wifi", "connect", ssid]
    if password:
        prompt += ["password", password]

    print("Connecting...")

    subprocess.run(prompt)

@cli.command()
def disconnect():
    proc = subprocess.Popen(["nmcli", "-t", "dev", "status"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if proc.wait():
        print(proc.stderr.read())
        return proc.returncode

    iflist_raw = proc.stdout.read().decode()
    iflist = [
            split_with_escaping(interface, ":")
            for interface in
            iflist_raw.split("\n")
    ][:-1]

    connected_wifi_interfaces = list(filter(lambda i: i[1] == "wifi" and i[2] == "connected", iflist))

    if len(connected_wifi_interfaces) > 1:
        print("Error: More than 1 connected wifi interface")
        exit(1)

    if len(connected_wifi_interfaces) == 0:
        print("Error: No connected wifi interfaces")
        exit(1)

    if_id = connected_wifi_interfaces[0][0]

    print(f"Disconnecting ({if_id})...")

    subprocess.run(["nmcli", "dev", "disconnect", if_id])

if __name__ == "__main__":
    cli()
