# arguments and keyword arguments in python i.e. 
#*args and **kwargs in python 

# remember destructuring in python was like 

a, b, *others = [1, 2, 3, 4, 5 , 6]

#now others is the list [3,4,5,6]

#similarily we can take arguments in a function like *args - args is just a convention, you can also use other words

def func(*args): 
  print(sum(args))
  print(args)

func(1,2,5,3,6)


#**kwargs in python are keyword arguments that is the arguments that 
# are sent with keywords to them. 

def func_kwargs(**kwargs): 
  print('here are the kwargs', kwargs) 

func_kwargs(hello = 23, thirsty = 'water_please')

def sum_func(*args, **kwargs): 
  print(sum(args) + sum(kwargs.values()))

sum_func(1,2,3,4,5,num1=65,num2=99)
#NOTE: args are in tuple where as kwargs are in a dictionary

# note that the convection for the order in which args and kwargs are sent to function are params, args, default_arguments, **kwargs 

def super_func(name, *args, phone_number=976044, **kwargs): 
  print('the name is:', name)
  print('The messages are:', args)
  print('the phone number is:', phone_number)
  print('Extra things are:', kwargs)


super_func('East Morningstar', 'Hey', 'Hello', "you there??", kit=9999, bathrooms=30)
#note that the default_arguments are the ones that are not mandatory because we have defined default value for them in the function declaration 


