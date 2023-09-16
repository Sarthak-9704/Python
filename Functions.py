# def mean( a=5,b=9 ):
#     m=(a+b)/(2)
#     print(m)

# mean(a=7)

# a=int(input("enter first number "))
# b=int(input("enter secind number "))

# mean(a,b)

# def fun():
#     a=int(input("enter a number"))
#     b=a*a
#     if(b%2==0):
#         print("square is even")
#     else:
#         print("number is odd")

# fun()
        
def fun():
    S=[]
    for i in range(90):
        if i%9==0:
            S.insert(i,i)
    return S

l=fun()
print(l)