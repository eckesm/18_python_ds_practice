def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels='AEIOUaeiou'
    vowel_str=''
    for char in s:
        if char in vowels:
            vowel_str+=char
    
    reversed_vowels=vowel_str[::-1]

    reversed_str=''
    index=0
    for char in s:
        if char in vowels:
            reversed_str+=reversed_vowels[index]
            index+=1
        else:
            reversed_str+=char
    
    return reversed_str
            