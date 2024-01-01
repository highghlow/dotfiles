import os
import click
import time

@click.command()
@click.argument("cmd")
def watch(cmd):
    if not os.path.exists("/proc/acpi/button/lid"):
        print("Unsupported platform")
        exit(1)

    lids = os.listdir("/proc/acpi/button/lid")

    if not lids:
        print("No lids found")
        exit(1)

    print("lidwatch started")

    prev_state = "open"
    while True:
        state = "closed"
        for lid in lids:
            with open(f"/proc/acpi/button/lid/{lid}/state") as f:
                if "open" in f.read():
                    state = "open"
                    break

        if prev_state == "open" and state == "closed":
            print("Running", cmd)
            os.system(cmd)
        
        prev_state = state


if __name__ == "__main__":
    watch()
