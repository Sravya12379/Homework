

import unittest

pin = input("please enter pincode")
n = 1
len = len(pin)


def len(pin):
    if len(pin) == 4:
        return "true"
    return "false"


bal = 100
wa = int(input("please enter withdrawl amount"))


def check(wa):
    if bal > wa:
        return "true"


def check_fails(wa):
    if bal < wa:
        return "false"


def main():
    print(check(90))


if __name__ == '__main__':
    main()