user_name = input('Enter your username')

user_password = input('Enter your password')

user_password_mask = '*'*len(user_password)

print('Hey {}, your password {} is {} long '.format(user_name, '*'*len(user_password), len(user_password)))

print(f'\n Hey {user_name}, your password {user_password_mask} is {len(user_password)} long ')

#----------------------------------------------------

birth_year = int(input("What year were you born?"))
print(f'You are {2022 - birth_year} year old bruh')


print(type(str(100)))

#-----------------------------------------------------------------

print(bin(6)) # binary number syntax, note number starts from 0b and then the binary representation
print(int('0b10101', 2)) #this will return the no. in integer. 2 is entered as we are giving base 2 number)

print(round(2.482, 2))
print(abs(-224))




#____________________________________________________________

#Fundamental Data types in python 

int 
float 
bool 
str
complex
list 
tuple 
set
dict 


# Classes: Custom data types in python


#Specialised data types - packages are available for these 

None # datatype in python for nothing



