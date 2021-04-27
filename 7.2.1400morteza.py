import random
A="123456789"
make=list()
i=0
while i<len(A):
    j=len(A)
    make2=list()
    while j>i:
        temp=int(A[i:j])
        make2.append(temp)
        j=j-1
    make.append(make2)    
    i=i+1
i=0
make[0].reverse() 
make[1].reverse()  
make[2].reverse()
make[3].reverse()
make[4].reverse()
make[5].reverse()
make[6].reverse()
make[7].reverse()
make[8].reverse()
print(make)
i=0
def app(A):
    C=list()
    i=0
    while i<len(A):
        C.append(A[i])
        i+=1
    return C
def sort(make,A,B,i):
    if i>=9:
        B.append(app(A))
        return   
    A.append(make[i][0])
    sort(make,A,B,i+1)
    A.pop()
    A.append(-make[i][0])
    sort(make,A,B,i+1)
    A.pop()
    if(i<8):
        A.append(make[i][1])
        sort(make,A,B,i+2)
        A.pop()
        A.append(-make[i][1])
        sort(make,A,B,i+2)
        A.pop()
    if(i<7):
        A.append(make[i][2])
        sort(make,A,B,i+3)
        A.pop()
        A.append(-make[i][2])
        sort(make,A,B,i+3)
        A.pop()
    if(i<6):
        A.append(make[i][3])
        sort(make,A,B,i+4)
        A.pop()
        A.append(-make[i][3])
        sort(make,A,B,i+4)
        A.pop()
    if(i<5):
        A.append(make[i][4])
        sort(make,A,B,i+5)
        A.pop()
        A.append(-make[i][4])
        sort(make,A,B,i+5)
        A.pop()
    if(i<4):
        A.append(make[i][5])
        sort(make,A,B,i+6)
        A.pop()
        A.append(-make[i][5])
        sort(make,A,B,i+6)
        A.pop()
    if(i<3):
        A.append(make[i][6])
        sort(make,A,B,i+7)
        A.pop()
        A.append(-make[i][6])
        sort(make,A,B,i+7)
        A.pop()
    if(i<2):
        A.append(make[i][7])
        sort(make,A,B,i+8)
        A.pop()
        A.append(-make[i][7])
        sort(make,A,B,i+8)
        A.pop()
    if(i<1):
        A.append(make[i][8])
        sort(make,A,B,i+9)
        A.pop()
        A.append(-make[i][8])
        sort(make,A,B,i+9)
        A.pop()    
        return
         
def sum(A):
    i=0
    sum1=0
    while i<len(B) :
        j=0
        while j<len(B[i]):
            sum1+=B[i][j]
            j+=1
        if sum1==100:
            print(B[i])
        sum1=0        
        i+=1  

A=list()
B=list()

sort(make,A,B,0)
sum(B)
       

        


    

