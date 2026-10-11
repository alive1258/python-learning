a =int(input())
b =int(input())
c =int(input())


# approce  1
# if a>= b:
#     if a>=c :
#         print(a," is the greatest")
#     else:
#         print(c," is the greatest")
# else:
#     if b>=c:
#         print(b," is the greatest")
#     else:
#         print(c," is the greatest")


# approce 2
if a>=b and a>=c:
    print(a," is the greatest")
elif b>=a and b>=c:
    print(b," is the greatest")
else:   
    print(c," is the greatest")
