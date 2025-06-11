x=int(input("enter your number"))
div=2
control=0
while div<x/2:
    if x%div==0:
        print("this is not a prime number")
        control=1
    else:
        div=div+1

if control==0:
     print(f"{x} is a prime number")
