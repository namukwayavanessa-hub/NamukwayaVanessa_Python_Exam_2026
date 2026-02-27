#question2 (i)
Student_Name= input('enter student name :')
Student_Number= input('enter student number:')
Mathermatics=int(input('enter mathematics marks:'))
Datasystems=int(input('enter Datasytems marks:'))
Web_Development=int(input('enter web deveolpment marks:'))
Avarage_mark= (Mathermatics + Datasystems + Web_Development) /3
print("Student Name:" ,Student_Name)
print("Student Number :" ,Student_Number)
print("Mathmatics:" ,Mathermatics)
print("Data systems : " ,Datasystems)
print("Wed Development : " ,Web_Development)
print(f"The Avarage_mark is {Avarage_mark:.2f}")

#question2(ii)
Distance_travelled=float(input('enter the distance travelled :'))
Fuel_used=float(input('enter the fuel used : '))
FuelEfficiency = Distance_travelled / Fuel_used
print("The distance travelled in kilometers is " ,Distance_travelled)
print("The fuel used in litres is " ,Fuel_used)
print(f"The car's fuel efficiency is {FuelEfficiency:.3f}")


#question2(iii)
for number in range(1 , 51):
      if number % 3==0:
            print (number)