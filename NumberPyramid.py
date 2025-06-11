def numberPyramide(rowsNumer):
    num=1
    for i in range(1,rowsNumer+1):
        for j in range(i):
            print(num,end="")
            num+=1
        print()

numberPyramide(4)