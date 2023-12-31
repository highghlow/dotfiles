import subprocess
import click
import json
from pick import pick

listype = list

def execute_and_read_json(command):
    output = subprocess.check_output(command)

    return json.loads(output)

@click.group()
def cli(): pass

@cli.group()
def list(): pass

def get_sources():
    return execute_and_read_json(["pactl", "-f", "json", "list", "sources"])

def get_sinks():
    return execute_and_read_json(["pactl", "-f", "json", "list", "sinks"])

def calculate_volume(sink):
    volume_components = []
    for direction in sink["volume"].values():
        volume_components.append( float( direction["value_percent"].rstrip("%") ) )
    return sum(volume_components) / len(volume_components)

@list.command()
def outputs():
    sinks = get_sinks()
    for sink in sinks:
        index = sink["index"]
        description = sink["description"]
        
        volume = round(calculate_volume(sink))
        
        muted = " (muted)" if sink["mute"] else ""

        print(f"{index}: {volume}%{muted} {description}") 

@cli.group()
def volume(): pass

def get_volume():
    default_sink_name = subprocess.check_output(["pactl", "get-default-sink"]).decode()[:-1]
    sinks = get_sinks()
    
    default_sink = listype(filter(lambda i: i["name"] == default_sink_name, sinks))[0]
    volume = calculate_volume(default_sink)
    return volume

def change_volume(volume):
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{volume}%"])

@volume.command()
@click.argument("by", type=float, default=10)
def up(by):
    change_volume(f"+{by}")
    print(round(get_volume()), "%", sep="")

@volume.command()
@click.argument("by", type=float, default=10)
def down(by):
    change_volume(f"-{by}")
    print(round(get_volume()), "%", sep="")

@volume.command()
@click.argument("to", type=float, default=100)
def set(to):
    change_volume(f"{to}")
    print(round(get_volume()), "%", sep="")

@volume.command()
def get():
    print(round(get_volume()), "%", sep="")

@volume.command()
def mute():
    subprocess.run(["pactl", "set-sink-mute", "@DEFAULT_SINK@", "true"])
    print("Muted")

@volume.command()
def unmute():
    subprocess.run(["pactl", "set-sink-mute", "@DEFAULT_SINK@", "false"])
    print("Unmuted")

@cli.group()
def set(): pass

@set.command()
def output():
    sinks = get_sinks()

    select = []

    description, selected = pick([
        i["description"] for i in sinks
    ], "Audio sinks:")

    new_name = sinks[selected]["name"]

    subprocess.run(["pactl", "set-default-sink", new_name])

    print(description)

@set.command()
def input():
    sources = get_sources()

    select = []

    description, selected = pick([
        i["description"] for i in sources
    ], "Audio sources:")

    new_name = sources[selected]["name"]

    subprocess.run(["pactl", "set-default-source", new_name])

    print(description)


if __name__ == "__main__":
    cli()



