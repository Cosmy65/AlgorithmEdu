x=int(input("enter a number"))
sum=0
while x!=0:
    print(f"the number that you enter({x}) is not equal to zero,be contunied")
    sum+=x
    x=int(input("enter a number"))
    if x==0:
        print("Oops! you have entered zero")
        break
print(f"sum={sum}")
