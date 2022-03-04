#Unlike lists like list(range(1000)) that will create a space in memory to hold this list from 0 to 999,
# generators return these numbers/ sequence items one at a time without storing them all in memory eg: for i in range(1000)

#note that generators in python are iterable, eg: for i in range(100). But not every iterable is a generator

#creating a generator

def generator_function(num):
    for i in range(num):
        yield i # note that the yield keyword pauses the function and comes back to it at a later time when we ask it to - by using the next keyword

for item in generator_function(100):
    print(item) # note that all this time, because of yield keyword, we only stored one item in memory at a time


g = generator_function(100) # note that this will not run the generator functiobecause of the yield keyword in. Unlike the functions with return/ no keyword in them,
# the function with a yield keyword does not run like this and instead assigns it to variable


print(g) # g is a generator object
print(next(g)) # prints 0. Note that next g returns the value of i for that particular iteration
print(next(g)) #prints 1
next(g)
print(next(g)) #prints 3

# note that the generator only stores the previous state of the function output


def generator_func2(num):
    for i in range(num):
        yield i

g = generator_func2(1)
next(g)
print(next(g)) # gives error, StopIteration

#note that generators are way more performant than iterators that are not generators

from time import time


def performance(func):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'this function took {t2 - t1} seconds')

    return wrapper_func


@performance
def generator_func(num):
    for i in range(num):
        i * 5


@performance
def iterator_func(num):
    for i in list(range(num)):
        i * 5


generator_func(10000000) #took .8 seconds
iterator_func(10000000) #took 1.1 seconds



#note that for loop uses generator under the hood, where it iterates through the iterable by using the next() method and automatically
#breaks when the StopIteration error occurs (the error that say for an array of length 5, when you try to access the 6th element)

#creating our own for loop to see how a for loop works under the hood

def special_for(iterable):
    iterator = iter(iterable)
    # note that iter method gives us the iterator for a particular iterable
    while True:
        try:
            print(iterator)
            print(next(iterator))  # next keyword till now we saw for running function to yield next generator. note it is also used to go forward with iterator (analogous to iterator++)
            # note that this wont work - iterable[iterator]
            # we use the value that next function returns as next function simply returns the element of iterable for that iterator and then does iterator++
        except StopIteration:
            break


special_for([8, 9 , 2, 3, 4, 8, 6])


# creating your own range class in python to understand generators better


class MyGenerator():
    currentValue = 0

    def __init__(self, start, end):
        self.start = start
        self.end = end

        # note that we can edit dunder methods for particular class like this as we read in dunders in python section

    def __next__(self):  # the next() method
        if MyGenerator.currentValue < self.end:
            MyGenerator.currentValue += 1
            return MyGenerator.currentValue
        raise StopIteration

    def __iter__(self):
        return self


for i in MyGenerator(0, 100):
    print(i)

# note that we know how for loop works under the hood

# it creates an iterator by using the iter() method on the iterable.

# it uses next() method on the iterator to go forward on the iterable

# note we return self on the iter() so that next() is run on it i.e.
# iterator = iter(iterable)

# for us iterator = MyGenerator class here
# so, next(iterator) will essentially be  next(MyGenerator) class here i.e. MyGenerator.__next__() will be executed

#printing Fibonacci numbers using generator because with list, we will run out of resources as fibonacci numebers explode fast

# create a fibonacci generator which can be used as for i in fib(21): print(i)

