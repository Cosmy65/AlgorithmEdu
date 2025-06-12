def oklid(a,b):
   while b!=0:
     temp=a%b
     a=b
     b=temp
   return a

num1=int(input("enter the first num"))
num2=int(input("enter the second num"))

oklid(num1,num2)

print(f"the obeb of {num1} and {num2}={oklid(num1,num2)}")
