def countdown(n):
    result = []
    while n != 0:
        result.append(n - 1)
        n -= 1
    return result

print(countdown(5))

def get_countdown(n):
    while n != 0:
        yield n - 1
        n -= 1

g = get_countdown(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


x = [i for i in range(10) if i >= 5]
print(x)
