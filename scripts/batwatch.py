import subprocess
import click
import glob
import time
import sys
import os

@click.command()
@click.argument("cmd")
@click.option("--low-level", type=int, default=20)
def watch(cmd, low_level):
    batteries = glob.glob("/sys/class/power_supply/BAT*")

    last_low = False
    while True:
        any_battery_low = False

        for battery_path in batteries:
            _, battery = os.path.split(battery_path)
            upower = subprocess.check_output(["upower", "-i", f"/org/freedesktop/UPower/devices/battery_{battery}"]).decode()

            for line_raw in upower.split("\n"):
                line = line_raw.strip(" ")

                if line.startswith("percentage:"):
                    percentage = line.lstrip("percentage:").lstrip(" ").rstrip("%")

                    if not percentage.isdigit():
                        print(f"Error getting capacity for {battery}: Capacity not an integer ({percentage})", file=sys.stderr)
                    else:
                        if int(percentage) < low_level:
                            any_battery_low = True

        if any_battery_low and not last_low:
            os.system(cmd)

        last_low = any_battery_low

if __name__ == "__main__":
    watch()
