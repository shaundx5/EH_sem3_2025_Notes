import time
import subprocess
from datetime import datetime

f = open("sudo_usage_log.txt", "a")

while True:
    result = subprocess.run(
        "journalctl _COMM=sudo --since=-1min",
        shell=True,
        capture_output=True,
        text=True
    )
    out = result.stdout

    for line in out.split('\n'):
        if line.strip():
            f.write(f"{datetime.now()} - {line.strip()}\n")

    f.flush()
    time.sleep(30)
