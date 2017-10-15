"""
    Interpolation Search
    -------------
    Partitions the list until the `key` is found.

    Time Complexity:  O(lg(lg n))

    Psuedo Code: https://en.wikipedia.org/wiki/Interpolation_search

"""


def interpolation_search(seq, key):
    """
    Takes a list of integers and searches if the `key` is contained within
    the list.

    :param seq: A list of integers
    :param key: The integer to be searched for
    :rtype: The index of where the `key` is located in the list. If `key` is
            not found then False is returned.
    """

    lo = 0
    hi = len(seq) - 1

    while (seq[hi] != seq[lo]) and (key >= seq[lo]) and (key <= seq[hi]):
        mid = lo + ((key - seq[lo]) * (hi - lo) // (seq[hi] - seq[lo]))

        if seq[mid] < key:
            lo = mid + 1
        elif key < seq[mid]:
            hi = mid - 1
        else:
            return mid

    if key == seq[lo]:
        return lo
    else:
        return False
