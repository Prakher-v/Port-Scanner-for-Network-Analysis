#This scoket liberary we used for connecting two nodes...
import socket
#This tremcolor liberary we used for make our output window look good and can find important things by different color.
import termcolor

def scanning(target, ports):

    print('\n' + ' Starting Scan For' + str(target))

    for port in range(1, ports):
        scanning_port(target, port)

def scanning_port(ipaddress, port):

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ipaddress, port))
        print(f'Port {port} is Opened')
        s.close()

    except:
        pass

targets = input("[*] Enter Target TO Scan(split them by \",\") : ")
ports = int(input("[*] Enter Number Of Ports To Scan : "))

if ',' in targets:

    print(tremcolor.colored(("[*] Scanning Multiple Tragets"), 'green'))

    for ip_add in targets.split(','):
        scanning(ip_add.strip(' '), ports)

else:

    scanning(targets, ports)