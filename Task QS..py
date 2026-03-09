#1.
class student:
    name:None
    age:None
    def __init__(self,n,a):
        self.name=n
        self.age=a
        print("Name:",self.name)
        print("Age:",self.age)

a=student("Logesh",21)
print("end".center(25,"*"))
b=student("loki",20)



#2.
class car:
    Brand:None
    Model:None
    Color:None
    Fuel:None
    price:None
    def __init__(self,B,M,C,F,P):
       
         self.Brand=B
         self.Model=M
         self.Color=C
         self.Fuel=F
         self.price=P
         print("Brand:",self.Brand)
         print("Model:",self.Model)
         print("Color:",self.Color)
         print("Fuel:",self.Fuel)
         print("price:",self.price)
n=car("Toyota","Fortuner","Black","petrol","45L")
print("CAR CREATED")


#3.
class Employee:
    ID=None
    Salary=None
    def __init__(self,I,S):
        self.ID=I
        self.Salary=S
        print("ID:",self.ID)
        print("Salary:",self.Salary)
c=Employee("12345","25k")


#4
class book:
    Name=None
    Author=None
    Price=None
    Zoner=None
    def __init__ (self,n,a,p,z):
        self.Name=n
        self.Author=a
        self.Price=p
        self.Zoner=z
        print("Name:",self.Name)
        print("Author:",self.Author)
        print("Price:",self.Price)
        print("Zoner:",self.Zoner)
b=book("The One","Jhone","200","action")
        

#5.
class calculator:
    def __init__(self,a,b,c):
        o=a+b+c
        print("D:",o)
c=calculator(1,2,3)
    
