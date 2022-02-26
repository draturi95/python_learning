# decorators in python

def hello():
    print('hello')


greet = hello

greet()  # prints hello as it runs hello function

del hello

greet()  # note that greet will still work and give us a printed hello

# note that functions in python act like variables. What python does when we say del hello is that it deletes the name reference hello to the function. It doesnt delete the function as greet is still pointing to it

# hence, greet() will continue to work

#note that functions in python behave like variable
def hello1(func):
    func()

def greet1():
    print('Im still here babe')

a = hello1(greet1) # this prints im still here babe


#higher order functions in python: -
#higher order funcions are functions that accept other functions as parameters  or functions that return another functions

#eg:

def greet3():
    def func():
        return 4
    return func

#next eg:
def greet4(func):
    func()


# decorators in python

# we understand it by defining our own decorator - just remember that decorators are basically used to super charge our functions

def my_decorator(func):
    def wrap_func():
        print('*****')
        func()
        print('*****')

    return wrap_func


@my_decorator
def say_hello():
    print('Hellooooo')


say_hello()

#remember very carefully - decorator takes the say_hello function as a parameter and returns the wrapper function.
# so if we have parameters in say_hello, they must go in the wrap_func as it is the one that is returned

def my_decorator1(func):
    def wrap_func1(name):
        print('*****')
        func(name)
        print('*****')

    return wrap_func1


@my_decorator
def say_hello6(name):
    print('Hellooooo,', name)


say_hello6('East')


# if we have multiple paramters in our function,
def my_decorator_mult(func):
    def wrap_func_mult(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')

    return wrap_func_mult


@my_decorator_mult
def say_hello(name, emoji=':)'):
    print('Hellooooo,', name, emoji)


say_hello('East')


# decorator in python to calculate how long it takes to run a function

# Decorator in python
from time import time


def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} seconds to run long_time function')
        return result

    return wrap_func


@performance
def long_time():
    for i in range(100000000): #might take over 20 seconds. for faster, remove a zero or two
        i * 5
    print('done')


long_time()


# decorator for authentication

user1 = {
    'name': 'Sorna',
    'valid': True
}


def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
        return fn(*args, **kwargs)
  return wrapper


@authenticated
def message_friends(user):
    print('message has been sent', user)


message_friends(user1)