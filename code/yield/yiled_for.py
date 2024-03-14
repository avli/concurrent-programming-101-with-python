from fib import fib


i = 0
for n in fib():
    print(n)
    i += 1
    if i == 5:
        break
