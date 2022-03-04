# note that we want to use generators and not lists to give out fibonacci numbers because we'll run out of resources in case of lists pretty quickly

# if we were to do this with a list, it would look like this:

def fib2(upper_limit):
    a = 0
    b = 1
    fibonax = []
    for i in range(upper_limit):
        fibonax.append(a)
        temp = b
        b = a + b
        a = temp

    return fibonax


for i in fib2(100):
    print(i)


# list takes a lot of time as can be seen by using the performance decorator we saw


# using generators with a class
class Fib:
    def __init__(self, number):
        self.upper_limit = number
        self.a = 0
        self.b = 1
        self.current = 1

    def __next__(self):
        if (self.current <= self.upper_limit):
            print(self.a)
            temp = self.a
            self.a = self.b
            self.b = temp + self.b
            self.current += 1
            return self
        raise StopIteration

    def __iter__(self):
        return self


# using generators in a function

def fib_func(upper_limit):
    a = 0
    b = 1
    if (upper_limit == 0):
        return a
    elif (upper_limit == 1):
        return b

    for i in range(0, upper_limit):
        yield a
        temp = b
        b = a + b
        a = temp

    return


for i in Fib(13):
    pass

for i in fib_func(100):
    print(i)

