def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    # return [item for item in l1 if l2.count(item) > 0]

    # incorporating suggested solutions:
    return [item for item in l1 if item in set(l2)]

    # or:
    # return list(set(l1) & set(l2))
