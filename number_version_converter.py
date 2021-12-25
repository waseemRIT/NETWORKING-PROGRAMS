"""
 Converts between number formats
 Convert an IPv4 Format from Binary to decimal  octet versions
 Convert an IPv4 Format from decimal octets to Binary Version

"""


def bin_to_decimal(bin):
    """
    :param bin: a string of 8 numbers -> 0 or 1
    :return: the decimal format of bin
    """
    my_decimal = 0
    index = 0
    while index < 8:
        # First Bit
        if index == 0:
            if bin[index] == "1":
                my_decimal = my_decimal + 128
        # Second Bit
        if index == 1:
            if bin[index] == "1":
                my_decimal += 64
        # Third Bit
        if index == 2:
            if bin[index] == "1":
                my_decimal += 32
        # Fourth Bit
        if index == 3:
            if bin[index] == "1":
                my_decimal += 16
        # Fifth Bit
        if index == 4:
            if bin[index] == "1":
                my_decimal += 8
        # Sixth Bit
        if index == 5:
            if bin[index] == "1":
                my_decimal += 4
        # Seventh Bit
        if index == 6:
            if bin[index] == "1":
                my_decimal += 2
        # Eighth Bit
        if index == 7:
            if bin[index] == "1":
                my_decimal += 1
        index += 1
    return str(my_decimal)


def ipv4_bin_to_dec(ipv4):
    """
    Converts an IPv4 from Binary Format to Decimal Format
    ip in binary -> nnn.nnn.nnn.nnn each nnn is an octet
    :param ipv4: has 8 bits in each octet
    :return: An str of the decimal version of each octet combined as an IPv4 Format
    """
    # Creates a list of
    the_ip = ipv4.split('.')
    ip_in_decimal = ""
    for octet in range(len(the_ip)):
        if octet == 3:
            ip_in_decimal += bin_to_decimal(the_ip[octet])
        else:
            ip_in_decimal += bin_to_decimal(the_ip[octet]) + "."

    return ip_in_decimal


def decimal_to_bin(decimal):
    decimal = int(decimal)
    my_binary = ""
    index = 0
    list_of_binaries = [128, 64, 32, 16, 8, 4, 2, 1]
    while index <= 7 :
        if ((decimal) - list_of_binaries[index]) >= 0:
            my_binary += "1"
            decimal -= list_of_binaries[index]
        else:
            my_binary += "0"

        index += 1

    return my_binary




def ipv4_dec_to_bin(ipv4):
    """
    ipv4 has 8 bits
    ipv4 is a string -> n.n.n.n
    """
    the_ip = ipv4.split('.')
    ip_in_binary = ""
    for octet in range(len(the_ip)):
        if octet == 3:
            ip_in_binary += decimal_to_bin(the_ip[octet])
        else:
            ip_in_binary += decimal_to_bin(the_ip[octet]) + "."

    return ip_in_binary


# Initializing Main
def main():
    print(ipv4_dec_to_bin("25.235.1.0"))

    print(ipv4_bin_to_dec("11101100.11101100.11101100.11101100"))


if __name__ == '__main__':
    main()
