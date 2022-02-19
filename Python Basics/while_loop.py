#while loops in python 
i = 0

while i < 10: 
  print(i)
  i+=1
else: 
  print('All work is done here') # note that once while condition is false, else is executed. Note that if while condition is false at the beginning, else will be executed and the loop will be exited

#note that we could have also written the print statement without else but else is useful in case we use break inside while loop, then else will also be skipped. 

i = 0

while i<10 : 
  print(i) 
  i+=1 
  break
else: 
  print(i) # note that break broke the loop else wasnt executed444

i = 0 
my_list = [1,2,3]

while(i< len(my_list)): 
  my_list[i]
  i+=1 


while True: 
  response = input('Say My Name')
  if(response == 'Dhawal'): 
    break