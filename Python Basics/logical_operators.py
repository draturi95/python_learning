#if then else statements in python are what we are studying today

is_old = 18
is_licensed = True

if is_old >= 18 and is_licensed: 
  print('Hey you can drive the car!!!!')
elif is_old > 16: 
  print('Hey please wait and soon you shall be able to drive')
else: 
  print('So sorry you arent old enough')
print('Checked and dusted!!!')


#ternary operators in python 
is_friend = True 
can_message = 'Yes' if is_friend else 'No'
print(can_message)

print('Ternary true ') if True else print("Ternary false")

#logical_operators 2 in python 

is_magician = True 
is_expert = False

if is_magician and is_expert: 
  print("you are a master magician")
elif is_magician and not is_expert: 
  print('Altease you are getting there')
else:
  print('You need magical powers')