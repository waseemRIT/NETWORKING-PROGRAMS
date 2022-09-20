import os, subprocess


def get_default_gateway():
    gateway = subprocess.run("ip route | grep default", shell=True, capture_output=True)
    # ip route | grep default
    ip_add = gateway.stdout.decode()
    try:
        gateway_ip_add = ip_add.split()[2]
        return gateway_ip_add
    except IndexError:
        return "DEFAULT GATEWAY NOT FOUND"


def ping_test(ip: str):
    # ping_result = subprocess.run(f"ping -c 4 {ip}", shell=True, capture_output=True)
    # print(ping_result)
    stream = os.popen(f"ping -c4 {ip}")
    output = stream.read()
    if '0 received' in output:
        return 'IP unreachable'
    else:
        return 'IP reachable'


def main():
    command = input("""Enter \"Gateway\" to test for Gateway connectivity.\nEnter \"it_dns\" to test for RIT DNS 
    connectivity\nEnter google.com  to resolve to test validity""")
    command.lower()

    if command == "gateway":
        gate_way_ip = get_default_gateway()
        print(f"The default Gateway: {gate_way_ip}")
        print(ping_test(gate_way_ip))
    elif command == "rit_dns":
        test_ip = "129.21.3.17"
        print(ping_test(test_ip))


if __name__ == '__main__':
    # while True:
    main()
