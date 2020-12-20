def fizz_buzz(n: int):
    """
    >>> fizz_buzz(6)
    1
    fizz
    buzz
    fizz
    5
    fizzbuzz
    """
    for i in range(1, n+1):  # i=1   n=6
        if i % 3 == 0 and i % 2 == 0:
            print('fizzbuzz')

        elif i % 2 == 0:
            print('fizz')

        elif i % 3 == 0:
            print('buzz')

        else:
            print(i)
