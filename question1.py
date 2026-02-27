#quetion 1(i)
def rectangle_area(length , widith):
    area= length * widith
    return area
print("The rectangle with length of 6 and widith of 3 it's area is ",rectangle_area(6 , 3))

# #qestion 1(ii)
number=[3 , 8 , 5 ,10, 11 ,14]
for n in number:
    if n % 2==0 :
      total = sum(n for n in number if n % 2== 0)
print('The sum of all even numbers in the list  is ', total)


#question1(iii)
def number_alg(x,y ,z):
    sum=x+y+z
    largest=max(x , y ,z)
    smallest= min(x , y , z)
    return sum  , largest , smallest
print("The sum , largest number and smallest number of three numbers is respectively" ,number_alg(10,2 ,7))



# #question 1(iv)
student_record={'name': 'Grace Nakato' , 'score':80 , 'grade': 'B'}
student_record['score']=95
student_record['school']='WITI'
print(student_record)


