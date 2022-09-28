#!/usr/bin/python3
# STUDENT: WASEEM QAFFAF
# DATE 28/09/22
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
import socket  # Library Used For DNS resolving utilities


def get_default_gateway():
    """
    Function used to get the default gateway of the device automatically
    returns
        the ip address of the default gateway -> #.#.#.#
    or
        returns 0
        if default gateway is not available
    """
    try:
        # USED TO RUN THE SHELL COMMAND TO GET THE DEFAULT GATEWAY IP ADDRESS
        # SUPPORTS OLD LINUX VERSIONS AND UP-TO-DATE VERSION
        gateway = subprocess.run(["sh", "-c", "ip route | grep default"], stdout=subprocess.PIPE)
        # GETS THE OUTPUT OF THE SHELL COMMAND USED | DECODES THE IP ADDRESS FROM b (binaries) to string
        ip_address = gateway.stdout.decode()
    except FileNotFoundError:
        # IF DEFAULT GATEWAY FILE IS NOT FOUND RETURN 0 SINCE THAT WOULD MEAN THAT THERE'S NO DEFAULT GATEWAY
        return 0
    try:  # TESTING IF AN IP ADDRESS WAS RETURNED
        gateway_ip_add = ip_address.split()[2]  # STRIPING THE IP ADDRESS FROM THE REST OF THE INPUT
        return gateway_ip_add
    except IndexError:
        # IF THERE IS NO IP ADDRESS RETURNED, IT WON'T BE ABLE TO GET THE SECOND INDEX AFTER USING split()
        return 0


def ping_test(ip: str):
    """
    Function used to test the connectivity of an IP ADDRESS
    returns
        IP reachable if the connectivity worked
            only when all packets get no reply
        IP unreachable the connectivity didn't work
    """
    # USING os.system() TO RUN THE ping SHELL COMMAND
    output = os.system(f"ping -c4 {ip}")

    # TESTING FOR ANY ERRORS
    if output == 0:
        return 'IP reachable'
    else:
        # MEANS THAT AN ERRORS OCCURRED IN THE PING COMMAND
        return 'IP unreachable'


def get_dns_ip(hostname: str):
    try:
        dns_ip = socket.gethostbyname(hostname)  # RESOLVES THE IP ADDRESS OF THE HOSTNAME
        return dns_ip  # RETURNS THE IP ADDRESS
    except:
        return 0


def exit_function():
    """
    FUNCTION TO EXIT THE PROGRAM
    """
    # os.system("exit")
    exit()


def getHeadline(size, char):
    return char * (size + 6)


def colorTextGreen(text):
    return "\033[32m" + text + "\033[0m"


def getHeader(sizeMargin, sizeTab, text):
    tab = '\t' * sizeTab
    header = tab + getHeadline(sizeMargin * 2 + 2 + len(text), '*') + '\n'
    sideMargin = '*' * sizeMargin

    return header + tab + sideMargin + ' ' + colorTextGreen(text) + ' ' + sideMargin + '\n' + header


def main():
    print(getHeader(3, 2, "Ping Test Troubleshooter"))
    # CREATING A MENU FOR THE USER TO CHOOSE FROM THE FUNCTIONS OPTIONS
    command = input("----------------------------------------------------------------------------------\n        Enter"
                    "1 to test for Gateway connectivity.\n        Enter 2 to test for RIT DNS "
                    "connectivity\n        Enter 3 google.com  to resolve to test validity\n        Enter 4 to "
                    "exit the program\n----->")

    command.lower()  # LOWERING THE INPUT OF THE USER JUST IN CASE

    if command == "1":  # IF USER INPUT MATCHES gateway IT WILL TEST FOR THE GATEWAY FUNCTION
        gate_way_ip = get_default_gateway()  # GETTING THE IP ADDRESS
        if gate_way_ip != 0:
            print(f"The default Gateway: {gate_way_ip}")  # PRINTING THE DEFAULT GATEWAY
            print(ping_test(gate_way_ip))  # PRINTING THE RESULT OF PINGING THE DEFAULT GATEWAY
        else:
            print("DEFAULT GATEWAY NOT FOUND")
    elif command == "2":  # IF THE USER INPUT MATCHES rit_dns IT WILL TEST FOR THE RIT DNS CONNECTIVITY
        test_ip = "129.21.3.17"
        print(ping_test(test_ip))  # PRINTING THE RESULT OF PINGING THE RIT DNS
    elif command == "3":  # IF THE USER INPUT MATCHES dns_testing IT WILL TEST FOR THE DNS CONNECTIVITY
        # GET THE HOSTNAME FROM THE USER
        hostname = input("What's the hostname: ")
        if hostname != "exit_func":
            # VARIABLE TO STORE THE VALUE OF THE  IP ADDRESS
            dns_ip = get_dns_ip(hostname)
            if dns_ip != 0:  # get_dns_ip returns 0 if an ERROR OCCURRED DURING RESOLVING HOSTNAME
                print(ping_test(dns_ip))  # PRINTING THE RESULT OF PINGING THE DNS/hostname
            else:  # SOMETHING WENT WRONG WITH RESOLVING THE IP ADDRESS
                print(
                    "DNS resolution NOT FOUND")
    elif command == "4":
        print("---------------------------------------------------------------------")
        print("EXITING PING TEST")
        exit_function()  # fUNCTION THE EXITS THE PROGRAM


if __name__ == '__main__':
    while True:  # KEEPS THE PROGRAM RUNNING TILL SOMEONE EXISTS USING CTRL + C
        try:
            main()
        except KeyboardInterrupt:
            # INFORMS THE USER THAT THE PROGRAM HAS STOPPED CAUSE OF CTRL+C
            print('Force Exit Because of Keyboard Interruption')
