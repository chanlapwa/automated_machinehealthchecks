"""
Objectives: checking the health of the machine, including
1) disk usage
2) cpu usage
3) localhost
4) connectivity
"""

#!/usr/bin/env python3
import shutil
import psutil
from network import *

def check_disk_usage(disk:str)->bool:
    """Verifies that there's enough free space on disk; free space more than 20% """
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage()->bool:
    """Verifies that there's enough unused CPU; cpu usage less than 75% """
    usage = psutil.cpu_percent(1)
    return usage < 75

# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
# Check the network connection if it's normal    
elif check_localhost() and check_connectivity():
    print("Everything ok")
# if network connection checks failed, print the warning message
else:
    print("Network checks failed")