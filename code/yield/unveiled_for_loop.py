from fib import fib


gen = fib()
iter(gen)

i = 0
while i < 5:
    n = next(gen)
    print(n)
    i += 1
