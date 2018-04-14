from string import ascii_lowercase

def number_needed(a, b):
    count = 0
    for letter in ascii_lowercase:
        ia = a.count(letter)
        ib = b.count(letter)
        count += abs(ia - ib)
    return count
    

a = input().strip()
b = input().strip()

print(number_needed(a, b))
