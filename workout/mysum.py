def mysum(*numbers):
    """
    Summing numbers
    :param numbers:
    :return:
    """
    output = 0
    for number in numbers:
        output += number
    return output
