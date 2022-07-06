"""
The function check_localhost() return true if the localhost of the machine
is correctly mapped to 127.0.0.1

The function check_connectivity() return true if the machine successfully 
connected to google.com
"""

#!/usr/bin/env python3
import requests
import socket
def check_localhost()->bool:
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'
def check_connectivity()->bool:
    request = requests.get("http://www.google.com")
    return request.status_code == 200