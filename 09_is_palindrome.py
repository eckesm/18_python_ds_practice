def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # adjusted_phrase = [char.upper() for char in phrase if char is not ' ']
    # reversed_phrase = [char.upper()
    #                    for char in phrase[::-1] if char is not ' ']
    # return adjusted_phrase == reversed_phrase

    # incorporating suggested solutions
    adjusted_phrase=phrase.lower().replace(' ','')
    return adjusted_phrase==adjusted_phrase[::-1]
