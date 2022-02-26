#error handling in python

#we can catch various errors in python, loosly speaking it is similar to how we do .catch in promises in js

# some common errors in python are: nameerror : when a variable is used before initialisation
#syntax error when python interpretor cant understand what to do with a line i.e. a syntax error has occured
#ZeroDivisionError error
#TypeError comes when two different types are being added, subracted etc. eg: adding a string and a number
#KeyError for accessing a key of an iterable that doesnt exist. Like array[25] in an array of length say 10, or obj['hh'] when hh key doesnt exist


#Error handling in python lets the program keep running even if it found an error and lets the program behave a certain way in case of an error

#Eg:
while True:
    try:
        age = int(input('what is your age? '))
        print(age)
    except:
        print("Age can only be a number")
    else:
        print('thankyou!!!')
        break


#Python first runs the try block, if it gives an error, except block is ran after try. If try doesnt give an error, else is run after try.

#note that we can handle errors in different blocks as well as shown below:

while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print("Age can only be a number")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
    else:
        print('thankyou!!!')
        break


#handling errors in a sum function

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('invalid number input given')
        print(err)
    else:
        print("Function call successful! Thankyou for your genuineness!!!")

sum(1, '2')


def div(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print('oops')
        print(err)

print(div(1, '2'))
print(div(1, 0))


while True:
    try:
        age= int(input('Please input your age'))
        10/age
    except ValueError as err:
        print('please enter a number')
        print(err)
    except ZeroDivisionError as err:
        print('Age cant be 0', err)
    else:
        print('thankyou')
        break
    finally:
        print('ok im done finally')

#input age cases: 0, 10, asdfsa



#note that python runs the try block first, if it throws error, except is ran and if try doesnt throw an error, else is run.
#Note that after an except/else is run, finally codeblock is run i.e. finally is run at the end of each iteration. Note in the above code, the break in else wont stop
#it from running finally .
#finally is ran before we break out of while


#note that in python, we can throw our own error and stop the code form running. We use the keyword raise for it
#for eg:
while True:
    try:
        age= int(input('Please input your age'))
        10/age
        raise ValueError('hey cut it out. Why would you give a valid age')
        #raise Exception('hey cut it out')
    except ZeroDivisionError as err:
        print('Age cant be 0', err)
    else:
        print('thankyou')
        break
    finally:
        print('ok im done finally')




