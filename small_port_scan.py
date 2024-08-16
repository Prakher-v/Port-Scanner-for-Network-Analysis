#!/bin/python
import sys
import socket
import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid number of arguments.")
    print("Usage: python port_scanner.py <ip>")

print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.datetime.now()))
print("-" * 50)

try:

    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))

        if result == 0:
            print(f"Port {port} is open")

        s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting...")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()
