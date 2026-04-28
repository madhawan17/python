a = 4
def square(a):
    return a*a 

print(square(a))

############
def square(a):
    return a**2
print (square(a))
#######################


def add(a,b):
    return a + b
print (add(2,3))

##############

def circle(r):
    a= 3.14*r**2
    c = 2*3.14*r
    return a,c
a,c = circle(5)

print ("area is :",a, "circumference is: ",c )