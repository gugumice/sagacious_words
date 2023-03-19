$ /usr/bin/env python3
import subprocess

while True:
    try:
        print subprocess.check_output(['python', 'testing.py'])
    except KeyboardInterrupt:
        break
