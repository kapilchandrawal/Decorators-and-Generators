
# 1) Implement Python's Range() Function.

def custom_range(stop, start = 0, increa = 1):
    lis = []
    while start < stop:
        print(start)
        lis.append(start)
        start = start + increa
    return lis
print(custom_range(5, 2))


