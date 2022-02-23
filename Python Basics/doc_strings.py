# Doc strings in python are used to store info about functions so
# in future when we hover over it, it tells what the function does
# other way from hover is to run help(fucn) or fucn.__doc__

def fucn():
    '''
    Info: Fuck you, Fuck you, Fuck you!!!
    '''
    print('Hello')


fucn()
help(fucn)

print(fucn.__doc__)
