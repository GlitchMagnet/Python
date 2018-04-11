'''
Title     : Python If-Else
Subdomain : Introduction
Language  : Python
Author    : Jacob Matini
Created   : 11 April 2018
'''

if __name__ == '__main__':

    import sys

    n = int(input().strip())
    w = 'Weird'
    nw = 'Not Weird'
    if n % 2 == 1:
        print(w)
    elif n % 2 == 0 and (n>=2 and n<5):
        print(nw)
    elif n % 2 == 0 and (n>=6 and n<=20):
        print(w)
    elif n % 2 == 0 and (n>20):
        print(nw)      
