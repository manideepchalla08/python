grade=(input("enter the grade of the employee"))
salary=int(input("enter the employee salary:"))
if(salary<=0):
  bouns=0
  print("enter the correct salary")
elif(grade=="a" ):
    bouns=5/100*salary
    print(bouns)
    print(bouns+salary)
elif(grade== "b"):
   bouns=10/100*salary
   print(bouns)
   print(bouns+salary)
elif(salary<=10000):
   bouns2=bouns+2/100*salary
   print(bouns2)
   print(bouns+salary)
elif(salary<=0):
   print("enter the correct salary")
else:
    print("incorrect input")
