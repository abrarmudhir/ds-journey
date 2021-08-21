def hex_output():
    """
    Hexadecimal output
    :return:
    """
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)
