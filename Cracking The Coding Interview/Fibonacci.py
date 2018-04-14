cache = {}
def fibonacci(n):
    if n < 2:
        return n
    if not n in cache.keys():
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]
n = int(input())
print(fibonacci(n))
