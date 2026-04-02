# python logical operator 
# and
# or
# not
a=5
b=3

print("a>10 and b>1:", a > 10 and b>1) # True and True = True
print("a>10 and b<1:", a>10 and b<1) # True and False = False
print("a>10 or b<1:", a>10 or b<1) # True or False = True
print("a<10 or b<1:", a<10 or b<1) # False or False = False
print("not a>10:", not a>10) # not True = False 
print("not a<10:", not a<10) # not False = True


marks =85

if marks >= 90 and marks <= 100:
    print("grade A")
elif marks >= 80 and marks < 90:
    print("grade B")
else:
    print("grade C")
