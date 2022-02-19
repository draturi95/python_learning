#global keyword in python 

total = 500 

def my_function(): 
  global total 
  total += 1 

my_function() 
print(total)

# note that if we had omitted line 6, we'd get an error as we never declared total inside my_function where total would be assumed to be a local variable. But since we want to access the global total, we use the global keyword for it in python

