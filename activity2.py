name = "Ayaan"
age = 16
is_student = True
weight = 60.5

print("Name :", name)
print("Data type of name is",type(name))
print("Age :", age)
print("Data type of age is",type(age))
print("is_student :", is_student)
print("Data type of is_student is ",type(is_student))
print("Weight :", weight)
print("Data type of weight is",type(weight))

print("/n after type casting")
age=str(age)
print(age)
print("Data type of age after type casting is",type(age))
weight=int(weight)
print(weight)
print("Data type of weight after type casting is",type(weight))

num1=50
num2=5
print("Number 1",num1)
print("Number 2",num2)
print("Sum = ",num1+num2)
print("Difference = ",num1-num2)
print("Product = ",num1*num2)
print("Division = ",num1/num2)
print("Floor division = ",num1//num2)
print("Modulus operation = ",num1%num2)
print("Square = ",num2**2)
print("Square root = ",num1**0.5)

print("Equal ?",num1==num2)
print("Number 1 greater ?",num1>num2)
print("Number 2 greater ?",num1<num2)
print("Not equal ?",num1!=num2)

result =num1/2+num2**2+10
print("Result of above equation is = ",result)
      