#!/usr/bin/python3

# STUDENT: WASEEM QAFFAF
# STUDENT ID: whq8052
# DATE 28/09/22
"""
There are 3 Options to this Program
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
        # sh starting the BASH (sh) shell | -c to run a command
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
        return f'YOUR DEVICE CAN SUCCESSFULLY CONNECT WITH {ip}'
    else:
        # MEANS THAT AN ERRORS OCCURRED IN THE PING COMMAND
        return f'YOUR DEVICE CANNOT CONNECT WITH {ip}'


def get_dns_ip(hostname: str):
    try:
        dns_ip = socket.gethostbyname(hostname)  # RESOLVES THE IP ADDRESS OF THE HOSTNAME
        return dns_ip  # RETURNS THE IP ADDRESS
    except:  # IF THERE'S NO IP ADDRESS
        return 0


def exit_function():
    """
    FUNCTION TO EXIT THE PROGRAM
    """
    # os.system("exit")
    exit()


def main():
    # CREATING A MENU FOR THE USER TO CHOOSE FROM THE FUNCTIONS OPTIONS
    command = input("\n\n----------------------------------------------------------------------------------\nEnter "
                    "Selection:\n\t1 - Test Connectivity to your gateway.\n\t2 - Test For Remote Connectivity.\n\t3 - "
                    "Test for DNS resolution.\n\t4 - Display gateway IP Address\nPlease enter a number (1-4) or quit/q"
                    " to quit the program.\n---> ")

    command.lower()  # LOWERING THE INPUT OF THE USER JUST IN CASE

    if command == "1":  # IF USER INPUT MATCHES 1 IT WILL TEST FOR THE GATEWAY FUNCTION
        gate_way_ip = get_default_gateway()  # GETTING THE IP ADDRESS
        if gate_way_ip != 0:
            if "SUCCESSFULLY" in ping_test(gate_way_ip):  # PRINTING THE RESULT OF PINGING THE DEFAULT GATEWAY
                print("DEFAULT GATEWAY CONNECTED SUCCESSFULLY")
        else:
            print("DEFAULT GATEWAY NOT FOUND ")

    elif command == "2":  # IF THE USER INPUT MATCHES 2 IT WILL TEST FOR THE RIT DNS CONNECTIVITY
        # RIT DNS:  129.21.3.17
        test_ip = "129.21.3.17"
        if "SUCCESSFULLY" in ping_test(test_ip):  # PRINTING THE RESULT OF PINGING THE RIT DNS
            print("RIT DOMAIN CONNECTED SUCCESSFULLY")
        else:
            print("RIT DOMAIN NOT UP")  # PRINTING THE RESULT OF PINGING THE RIT DNS

    elif command == "3":  # IF THE USER INPUT MATCHES 3 IT WILL TEST FOR THE remote CONNECTIVITY
        hostname = "google.com"
        # VARIABLE TO STORE THE VALUE OF THE  IP ADDRESS
        dns_ip = get_dns_ip(hostname)
        if dns_ip != 0:  # get_dns_ip returns 0 if an ERROR OCCURRED DURING RESOLVING HOSTNAME
            print(ping_test(dns_ip))  # PRINTING THE RESULT OF PINGING THE DNS/hostname
            print("THIS IS THE google.com IP AFTER RESOLUTION")
        else:  # SOMETHING WENT WRONG WITH RESOLVING THE IP ADDRESS
            print(
                "google.com DNS resolution to IP not found")

    elif command == "4":  # IF THE USER INPUT MATCHES 4 IT WILL GRAB THE DEFAULT GATEWAY AND PRINT IT
        gate_way_ip = get_default_gateway()  # GETTING THE IP ADDRESS
        if gate_way_ip != 0:  # Checking if IP ADDRESS EXISTS
            print(f"The Default Gateway: {gate_way_ip}")  # PRINTING THE DEFAULT GATEWAY
        else:
            print("DEFAULT GATEWAY NOT FOUND")  # there's no default gateway in the device

    elif command == "quit" or command == "q":
        print("---------------------------------------------------------------------")
        print("EXITING PING TEST")
        exit_function()  # fUNCTION THE EXITS THE PROGRAM

    else:
        # AN INVALID OPTION WAS GIVEN AN INPUT
        print("INVALID INPUT TRY AGAIN PLEASE!!\n")


if __name__ == '__main__':
    os.system("clear")  # CLEAR ALL PAST OUTPUTS
    while True:  # KEEPS THE PROGRAM RUNNING TILL SOMEONE EXISTS USING CTRL + C
        try:
            main()
        except KeyboardInterrupt:
            # INFORMS THE USER THAT THE PROGRAM HAS STOPPED CAUSE OF CTRL+C
            print('\nForce Exit Because of Keyboard Interruption\n')
            exit_function()
