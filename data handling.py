#  **.txt files**
with open("test.txt","w") as f:
    f.write("hello \nworld")
    

with open("test.txt","r" ) as l:
    p=l.readline()
    print(p)

with open("test.txt", "a") as k:
    k.write("\nthis is a text file")

import os.path


a=int(input("1 for reading, 2 for new file, 3 for appending file, 4 for seeking, 5 to write in binary "))
if(a==1):
    b=input("enter name of txt file ")
    try:

        with open(b+".txt","r" ) as l:
            p=l.read()
            print(p)
    except:
        print("file not found ")
elif (a==2):
    filename=input("enter name of new file ")
    filename=filename+'.txt'
    if os.path.exists(filename):
        print("file already exists. now opening in append mode ")
        with open(filename, "a") as file:
            app=input("enter what you wish to write into file ")
            file.write(app+'\n')
    else:
        with open(filename,"w") as file:
            app=input("enter what you wish to enter in file ")
            file.write(app)
elif (a==3):
    filename=input("enter name of file you wish to append")
    filename=filename+'.txt'
    if os.path.exists(filename):
        with open(filename, "a") as file:
            app=input("enter what you wish to write into file ")
            file.write(app+'\n')
    else:
        print("file does not exist")
elif (a==4):
    filename=input("enter name of new file ")
    filename=filename+'.txt'
    if os.path.exists(filename):
        with open(filename, "r") as file:
            search=int(input("which position do you wish to seek "))
            file.seek(search)
            c=file.read(search)
            print(c)
elif (a==5):
    filename=input("enter name of file ")
    filename=filename+'.txt'
    if os.path.exists(filename):
        with open(filename, 'wb') as file:
            # app=input("enter what you wish to write into file ")
            file.write(b"hello world")
        
#  **pickles**
import pickle
with open("dress.dat","wb") as F:
  pickle.dump({'ID':1,"Qty":45},F)

with open("dress.dat","rb") as F:
  print(pickle.load(F))

#   **csv files**

names = ['sar', 'sid', 'jay', 'sus']
marks = [92,91,90,87]
import csv
# with open("csv_test.csv", "w", newline="") as file:
#     file=csv.writer(file, delimiter=',')
#     file.writerow(names)
import math
#     file.writerow(marks)
rad = []
area = []
circum = []
i=0

for i in range(9):
    rad.append(i)
    circum.append(2*3.14*i)
    area.append(3.14*i*i)
    
area.pop()
area.pop()
with open("circles.csv", 'w', newline="") as file:
    f=csv.writer(file)
    f.writerow(['radius', 'area', 'circumference'])
    for i in range(9):
        inp=[rad[i],area[i],circum[i]]
        f.writerow(inp)
    
    
