#question4(i)
# OOP is a programming style that organizes code using objects and classes

#importance 
# OOP is fast in we development
#It's easy maintance
#Resuability


 # Inheritance is a core OOP concept where one class acquires the properties and behaviors  (fields and methods) of another class .
# Real_world example:
# A Vehicle can move and has wheels.
# A Car is a type of Vehicle, but it also has extra features like doors and air conditioning



#question4(ii)
text=str(input('enter a sentence:'))
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(" The number of vowels in the entered text is ", count)



#quetion4(iii)
def numbers(x , y):
    product= x * y
    return product
print( "The function with values x = 6 and y= 7 its product is " ,numbers(6 ,7))





 
    