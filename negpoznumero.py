number=[]
neqativeNum=[]
pozitiveNum=[]
poz=0
neq=0
for i in range(1,5):
    num=int(input(f"enter {i}. number:"))#f"" dikkat
    number.append(num)

print("all numeros",number)

for num in number:
    if num>0:
        pozitiveNum.append(num)
        poz = poz + 1
    elif num<0:
        neqativeNum.append(num)
        neq=neq+1





print("all pozitive numeros",pozitiveNum)
print(f"there are {poz}  pozitive numbers" )
print("all negative numerss",neqativeNum)
print(f"there are {neq} neqative numbers")