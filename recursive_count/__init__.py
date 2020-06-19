'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # Count Reference
    count = 0
    # If the length is less than 2 return count
    if len(word) < 2:
        return count
    # Else check for 'th' using splicing
    else:
        # If found iterate count
        if word[:2] == 'th':
            count += 1
    # Remove the first character from the string
    word = word[1:]
    # Recurse until the length is less that two
    # Then return the total count
    return count + count_th(word)
