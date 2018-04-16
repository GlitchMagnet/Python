import string

def capitalize(string):
    s = string.split(' ')
    return ' '.join((word.capitalize() for word in s))
