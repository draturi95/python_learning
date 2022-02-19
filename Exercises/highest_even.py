def highest_even(*args): 
  num_list = list(args) 
  max = -9999
  for num in num_list: 
    if(num > max and num % 2 == 0):  
      max = num 
  return max 

print(highest_even(1,2,3,98,45,576))


  