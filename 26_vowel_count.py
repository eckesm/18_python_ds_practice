def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = {}
    for char in phrase.lower():
        if char.lower() in 'aeiou':
            # if char in vowels:
                # vowels[char] = vowels[char] + 1
            # else:
                # vowels[char] = 1
            vowels[char.lower()]=vowels.get(char.lower(),0)+1
    return vowels

# suggested solution incorated