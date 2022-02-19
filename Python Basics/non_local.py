#nonlocal keyword in python 

# note that the global keyword in python was used to tell the interpreter that we'll be using the global variable. But say that if the variable we wanna use from outside the function is not global but just not local, we use non local keyword 

def outer(): 
  x = 'local'
  def inner(): 
    nonlocal x 
    x = 'local changed'
    print('inner:', x)
  
  inner() 
  print('outer: ', x)

outer()

#note that in the above case, we wanted to use x but it wasnt local and it wasnt global. So, we used the nonlocal keyword to access it and note that we can even change it inside function inner