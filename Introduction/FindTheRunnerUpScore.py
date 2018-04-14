'''
Domain    : Python
Subdomain : Introduction
Author    : Jacob Matini
Created   : 11 April 2018
'''

if __name__ == '__main__':
    
    n = int(input())
    
    print(sorted(list(set(map(int, input().split()))))[-2])
