#short circuiting in python

is_friend = True  
is_user = False 

if is_friend or is_user:
  print('BFF')
else:
   print('Not really')

  #note that python wont check the second condition in the 
  #if condition_1 or condition_2 if condition_1 is true as it now knows that it must run the if's statement 
