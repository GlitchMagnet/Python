import sys

def distinctPairs(k, arr):
    sorted_array = list(sorted(arr))
    check = set()
    answer = 0
    for i in sorted_array:
        if k - i in check:
            answer += 1
        if i == i - 1
			answer += 1	
        check.add(i)
    return answer

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = distinctPairs(k, arr)
    print(result)
