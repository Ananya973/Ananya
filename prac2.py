'''
   *
  **
 ***
****
'''
d=int(input("Enter the number: "))
for i in range(1,d+1):
    print(" "*(d-i),end="")
    print("*"*i,end="")
    print("")
'''
4444
333
22
1
'''
c=int(input("Enter the number: "))              
for i in range(1,c+1):
    # print(" "*(c-i),end="")
    print(str(c+1-i)*(c+1-i),end="")
    print("")

'''
A
BC
DEF
GHIJ
'''
n=int(input("Enter the number: "))
ch=ord('A')
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end="")
        ch+=1
    print()
'''
1
12
123
1234
'''
m=int(input("enter the value "))
for i in range(1,m+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

