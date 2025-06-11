
rows=4

for i in range(1,rows+1):#ilk başta boşluklar
    print(" "*(rows-i),end=" ")
    for j in range(i):#j aslında hiç değişmeyecek değişen artan i'ler olacak
        print("*",end=" ")#end yan yana yazdırmayı sağlar
    print()