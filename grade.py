a=input("Enter marks of first subject")
a=int(a)
b=input("Enter marks of second subject")
b=int(b)
c=input("Enter marks of third subject")
c=int(c)
d=input("Enter marks of fourth subject")
d=int(d)
e=input("Enter marks of fifth subject")
e=int(e)
sum=a+b+c+d+e
pr=sum/100
if pr>=90:
    print("Grade A")
elif pr>=80:
    print("Grade B")
elif pr >= 70:
    print("Grade C")
elif pr >= 60:
    print("Grade D")
elif pr >= 70:
    print("Grade E")
else:
    print("Failed")

