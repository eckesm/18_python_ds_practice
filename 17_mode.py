def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # most_common = ['', 0]
    # for (k, v) in {num: nums.count(num) for num in nums}.items():
    #     if v > most_common[1]:
    #         most_common = [k, v]
    # return most_common[0]

    # incorporating suggested solution:
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0)+1

    max_value = max(counts.values())
    for (num, freq) in counts.items():
        if freq == max_value:
            return num
