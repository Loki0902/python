'''
w=open(r"/Users/logesh/Desktop/loki.txt","a")
w.write("\n Hi")
w.close()
print("file writted")


m=open(r"/Users/logesh/Desktop/pri.txt","w")
m.write(" do another mini project")
m.close()

import os
os.remove(r"/Users/logesh/Desktop/loki.txt")


try:
    a=10
    b=0
    c=2
    print(a+b)
    print(a-b)
    print(a/b)
except Exception as e :
 print(e)
finally:
    print("program finished")
    


#assert
a=10
assert a<101
print(a)
'''
try:
    a=10
    b=5
    c=2
    if b==0:
        raise zero_division_error ("cannot divide by zero")
    print(a+b)
    print(a-c)
    print(a/b)
except Exception as e:
    print(e)
