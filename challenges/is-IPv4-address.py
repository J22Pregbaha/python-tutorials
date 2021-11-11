# An IP address is a numerical label assigned to each device (e.g., computer, printer) participating
# in a computer network that uses the Internet Protocol for communication.
# There are two versions of the Internet protocol, and thus two versions of addresses.
# One of them is the IPv4 address.
#
# Given a string, find out if it satisfies the IPv4 address naming rules.
def isIPv4Address(inputString):
    numbers = inputString.split(".")

    if len(numbers) != 4:
        return False

    for i in numbers:
        if not i.isnumeric():
            return False
        elif len(str(int(i))) != len(i):
            return False
        elif not int(i) in range(256):
            return False

    return True

print(isIPv4Address("64.233.161.00"))
