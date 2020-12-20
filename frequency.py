def count_letters(s: str):
    """
    >>> count_letters('diego')
    {'d': 1, 'i': 1, 'e': 1, 'g': 1, 'o': 1}

    >>> count_letters('Ddiego')
    {'D': 1, 'd': 1, 'i': 1, 'e': 1, 'g': 1, 'o': 1}

    >>> count_letters('banana')
    {'b': 1, 'a': 3, 'n': 2}

    """

    result = {}
    for letter in s:  # letter = d
        result[letter] = result.get(letter, 0) + 1  # {'d': 1}

    return result
