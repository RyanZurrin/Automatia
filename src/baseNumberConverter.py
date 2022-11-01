# convert any given number into it's equivalent in any base from 0 to 36
#

import string


def base_converter(number, base):
    digits = string.digits + string.ascii_uppercase
    if number < base:
        return digits[number]
    else:
        return base_converter(number // base, base) + digits[number % base]


def main():
    print(base_converter(10, 2))
    print(base_converter(10, 8))
    print(base_converter(10, 16))
    print(base_converter(10, 36))
    print(base_converter(2, 1))


if __name__ == '__main__':
    main()