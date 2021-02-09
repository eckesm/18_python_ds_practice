def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    open_p = 0
    closed_p = 0
    for char in parens:
        if char == "(":
            open_p += 1
        if char == ")":
            closed_p += 1
        if closed_p > open_p:
            return False
    if open_p == closed_p:
        return True
    return False
