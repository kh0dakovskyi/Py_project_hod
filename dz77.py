def func():
    n = 0
    while True:
        yield 3 ** n
        n += 1

gen = func()
for i in range(10):
    print(next(gen))
