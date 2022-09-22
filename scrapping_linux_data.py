"""
There are 3 Functions to this Program
1. Testing the connectivity of the default gateway
    note:default gateway is processed automatically
2. Testing the RIT DNS connectivity
    note: RIT DNS ip address is hard codded: "129.21.3.17"
3. Does two things:
    a. Resolves a DNS/hostname to an IP Address
    b. Testes the connectivity to that DNS/hostname
"""

import os  # Library Used For Pinging Utilities
import subprocess  # Library used For Shell Commands Utilities


def get_default_gateway():
    """
    Function used to get the default gateway of the device automatically
    returns
        the ip address of the default gateway
    or
        DEFAULT GATEWAY NOT FOUND
    """
    # USED TO RUN THE SHELL COMMAND TO GET THE DEFAULT GATEWAY IP ADDRESS
    gateway = subprocess.run("ip route | grep default", shell=True, capture_output=True)
    # GETS THE OUTPUT OF THE SHELL COMMAND USED | DECODES THE IP ADDRESS FROM b to string
    ip_add = gateway.stdout.decode()
    try:  # TESTING IF AN IP ADDRESS WAS RETURNED
        gateway_ip_add = ip_add.split()[2]  # STRIPING THE IP ADDRESS FROM THE REST OF THE INPUT
        return gateway_ip_add
    except IndexError:
        # IF THERE IS NO IP ADDRESS RETURNED, IT WON'T BE ABLE TO GET THE SECOND INDEX AFTER USING split()
        return "DEFAULT GATEWAY NOT FOUND"


def ping_test(ip: str):
    """
    Funtion used to test the connectivity of an IP ADDRESS
    returns
        IP reachable if the connectivity worked
            only when all packets get no reply
        IP unreachable if the connectivity didn't work
    """
    # USING os.system() TO RUN THE ping SHELL COMMAND
    output = os.system(f"ping -c4 {ip}")
    # COMMAND TO GET THE OUTPUT OF THE ping COMMAND
    # output = stream.read()
    # TESTING FOR ANY ERRORS
    if output == 0:
        return 'IP reachable'
    else:
        # MEANS NO ERRORS RAN IN THE PING COMMAND
        return 'IP unreachable'


def get_dns_ip(hostname: str):
    dns_ip = subprocess.run(f"nslookup {hostname}", shell=True, capture_output=True)
    dns_ip_resolved = dns_ip.stdout.decode()
    if "server can't find" in dns_ip_resolved:
        return "DNS NOT FOUND"
    else:
        dns_ip = subprocess.run(f"nslookup {hostname} | grep -i server: | cut -d\":\" -f2", shell=True,
                                capture_output=True)
        return dns_ip.stdout.decode().strip()


def main():
    # CREATING A MENUE FOR THE USER TO CHOOSE FROM THE FUNCTIONS OPTIONS
    command = input("----------------------------------------------------------------------------------\n1.Enter "
                    "\"gateway\" to test for Gateway connectivity.\n2.Enter \"rit_dns\" to test for RIT DNS "
                    "connectivity\n3.Enter \"dns_testing\" google.com  to resolve to test validity\n----->")
    command.lower()  # LOWERING THE INPUT OF THE USER JUST IN CASE
    if command == "gateway":  # IF USER INPUT MATCHES gateway IT WILL TEST FOR THE GATEWAY FUNCTION
        gate_way_ip = get_default_gateway()  # GETTING THE IP ADDRESS
        print(f"The default Gateway: {gate_way_ip}")  # PRINTING THE DEFAULT GATEWAY
        print(ping_test(gate_way_ip))  # PRINTING THE RESULT OF PINGING THE DEFAULT GATEWAY

    elif command == "rit_dns":  # IF THE USER INPUT MATCHES rit_dns IT WILL TEST FOR THE RIT DNS CONNECTIVITY
        test_ip = "129.21.3.17"
        print(ping_test(test_ip))  # PRINTING THE RESULT OF PINGING THE RIT DNS

    elif command == "dns_testing":  # IF THE USER INPUT MATCHES dns_testing IT WILL TEST FOR THE DNS/hostname
        # CONNECTIVITY
        hostname = input("What's the hostname: ")
        dns_ip = get_dns_ip(hostname)
        print(ping_test(dns_ip))  # PRINTING THE RESULT OF PINGING THE DNS/hostname


if __name__ == '__main__':
    while True: # KEEPS THE PROGRAM RUNNING TILL SOMEONE EXISTS USING CTRL + C
        main()
