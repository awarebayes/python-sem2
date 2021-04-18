from timeit import timeit

time = lambda f: timeit(f, number=1)

arr = [*[-2, 4, 1, 4, 2, 4, 5] * 100]


def sort_time(arr):
    return time(lambda: sorted(arr))


print(sort_time(arr))
