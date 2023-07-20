
b=0

for a in range(1,10):
    c=0
    while(b<(a)):
        if(a%b==0):
            c=c+1
        b=b+1
    if(c>0):
        print(a)
    
    a=a+1
    # print("helo")