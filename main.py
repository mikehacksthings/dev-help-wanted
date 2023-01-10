def remove_odds(nums: set[int]) -> set[int]:
    """ remove all off numbers from a set of integers

    Args:
        nums (set): set of integers to remove odd numbers from

    Returns:
        set[int]: set of integers without odd numbers
    """
    #TODO: implement this function
    return set(x for x in nums if not x % 2)


def vowel_captilization(string: str) -> str:
    """ capitalize all vowels in a string and lowercase all consonants

    Args:
        string (str): string to capitalize

    Returns:
        str: string with all vowels capitalized and all consonants lowercased
    """
    #TODO: implement this function
    vowels = ['a', 'e', 'i', 'o', 'u']
    ret = ""
    for c in string:
        if c.lower() in vowels:
            ret += c.upper()
        else:
            ret += c.lower()
    return ret


