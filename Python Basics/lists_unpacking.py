#list unpacking 


#2 
a,b,c,*other = [1,2,3,4,5,6,7]
print(a)
print(b)
print(c)
print(other, ' this is the other')


#3

#2 
a,b, *another, c = [1,2,3,4,5,6,7]
print(a)
print(b)
print(c)
print(another, ' this is the another')



#1
a,b,c = [1,2,3]

print(a)
print (b) 
print(c)