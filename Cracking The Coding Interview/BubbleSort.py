n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0

while True:
    SwapsFlag = False
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            numSwaps += 1
            SwapsFlag = True
    if not SwapsFlag:
        break


print('Array is sorted in', numSwaps, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])
