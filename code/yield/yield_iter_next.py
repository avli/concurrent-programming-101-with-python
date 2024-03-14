def f():
    yield 'foo'
    yield 'bar'
    yield 'baz'


gen = f()
iter(gen)
print(next(gen))
print(next(gen))
print(next(gen))
try:
    next(gen)
except StopIteration:
    print('Nothing else to yield')
