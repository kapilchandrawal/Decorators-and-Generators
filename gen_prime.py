
#2) Write the generator Function to print prime Numbers.

def prime_generator(limit):
    yield 2
    start = 3 
    for i in range(start, limit+1):
        flag = True
        for j in range(2,i):
            if(i % j == 0):
                flag = False
        if(flag):
            yield i

x = prime_generator(5) 
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())


