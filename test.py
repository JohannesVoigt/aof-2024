from timeit import timeit

SIZE = 1_000
NUM = 1_000

list_ = [list(range(SIZE)) for _ in range(SIZE)]

# print([*zip(*list_)])
print(timeit("[*zip(*list_)]", globals=globals(), number=NUM))
# print(list(zip(*list_)))
print(timeit("list(zip(*list_))", globals=globals(), number=NUM))
# print([*map(list, zip(*list_))])
print(timeit("[*map(list, zip(*list_))]", globals=globals(), number=NUM))
# print(list(map(list, zip(*list_))))
print(timeit("list(map(list, zip(*list_)))", globals=globals(), number=NUM))
# print([list(x) for x in zip(*list_)])
print(timeit("[list(x) for x in zip(*list_)]", globals=globals(), number=NUM))
