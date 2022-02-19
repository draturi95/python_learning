# walrus operator in python 

#:= is used to assign to a variable in the same expression as it is being used 


a = 'hellooooooo'

if(len(a) > 10) : 
  print('The length of the string {} is a very large numebr for the string to be printed'.format(len(a)))

  # now instead of above, we could have done 

if((n := len(a))): 
  print('The length of the string {} is a very large numebr for the string to be printed'.format(n))


while((n:= len(a)) > 1): 
  print(n) 
  a = a[:-1]