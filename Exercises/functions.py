def small_talk(): 
  name = input("Hey what's your name?" )
  print('Hello there!',name)

small_talk()

def small_talk2(name):
    print('Hello there!',name)

name = input("hey whats your name? ")

small_talk2(name)


#note that we can also give function parameters in different orders than defined in funciton definition

#say function is func(num1, num2, operator) 
# we can call it like func(num2 = 9, operator = '*', num1 = 8)


#note that we can just like js and graphql, give default values to various parameters in python function in its definition as: 

# def func(name="nameLess", age='ageless')
  #....function code inside. Now name and age parameters have default values which will be used when a /both parameters missed when calling the function

def factorial(number):
  answer = 1
  for i in range(1,number + 1): 
    answer *= i
  return answer

print(factorial(5))


