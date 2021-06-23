print("Enter three angles of triangles")
a=input("Enter first angle")
a=int(a)
b=input("Enter second angle")
b=int(b)
c=input("Enter third angle")
c=int(c)
d=a+b+c

if d==180:
    print("The angles form a triangle")
else:
    print("The angles does not form a triangle")