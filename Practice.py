''' 
    * 
   *** 
  ***** 
 ******* 
********* '''
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print(" ")

a=int(input("Enter the number: "))
for i in range(1,a+1):
    if (i==1 or i==a):
        print("*"*(a),end=" ")
    else:
        print("*",end="")
        print(" "*(a-2),end="")
        print("*",end="")
    print(" ")
    

m=int(input("Enter the number: "))
for i in range(1,m+1):
    print(" "*(m-i),end="")
    print(str(i)*(2*i-1),end="")
    print(" ")

g=int(input("Enter the number: "))
for i in range(1,g+1):
    print("*"*g,end="")
    print("")

d=int(input("Enter the number: "))
for i in range(1,d+1):
    print("*"*i,end="")
    print("")

c=int(input("Enter the number: "))
for i in range(1,c+1):
    print(str(i)*i,end="")
    print("")