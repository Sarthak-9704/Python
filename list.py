marks = [1,2,3,4,5,6,7,8]

print(marks[0])

if "he" in marks:
    print("yes")

print(marks[1:]) # slicing

print(marks[4:-2])

print(marks[0:8:2])

lst = [i+1 for i in range(5) ]
print(lst)

l = [1,1,2,2,3,3,1,2,3,6,5,4]

print(l.count(1))

l.insert(3,999)
print(l[3])

l.extend (lst)
print (l)

m= l.copy()
print(m)