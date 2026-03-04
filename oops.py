'''class demo:
    name="loki"
    age="20"
    def fun1(self):
        print("Hello logesh...")
d=demo()
print(d.name)
print(d.age)
d.fun1()

class car:
    Brand=None
    model=None
    color=None
    fuel=None
    price=None
    def engine(self):
        print(self.brand,"car engine start,run,stop..")
        print("END".center(25,"*"))
c1=car()
c1.brand="TATA"
c1.model="NEXON"
c1.color="Blue"
c1.fule="petrol"
c1.price="1500000"
print("brand:",c1.brand)
print("model:",c1.model)
print("color:",c1.color)
print("fule:",c1.fule)
print("price:",c1.price)
c1.engine()
'''
class mobile:
    Brand=None
    model=None
    color=None
    Ram=None
    Camera=None
    price=None
    def __init__(self,b,m,c,r,cam,p):
        self.Brand=b
        self.model=m
        self.color=c
        self.Ram=r
        self.Camera=cam
        self.price=p
        print("Brand:",self.Brand)
        print("Model:",self.model)
        print("Color:",self.color)
        print("Ram:",self.Ram)
        print("Camera:",self.Camera)
        print("Price:",self.price)
m1 = mobile("Samsung","S26","Red","12 GB","50 MP","125000")
print("END".center(25,"*"))
m2 = mobile("Apple","16 Pro","Black","16 GB","108 MP","145000")

      
        
























    
    
