def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    dict1 = {}
    for digit in str(num1):
        if digit in dict1:
            dict1[digit] = dict1[digit]+1
        else:
            dict1[digit] = 1

    dict2 = {}
    for digit in str(num2):
        if digit in dict2:
            dict2[digit] = dict2[digit]+1
        else:
            dict2[digit] = 1

    return dict1 == dict2
