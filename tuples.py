#similar to lists but cannot be changed
#use parenthesis while lists use square brackets

tup = (1,3,5,7)

print(type(tup))

# tup.append (1) gives error as tuple cannot be editted

# tup2 = tup.copy()  gives error

temp = list(tup)

temp.append(999)

tup = tuple(temp)

print (tup)

t1 = (1,2,3,4)
t2 = (5,6,7,8)

t3= t1+t2
print(t3)