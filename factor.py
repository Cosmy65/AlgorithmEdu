x=int(input("enter a number"))
divid=2
factors=[]
while x>1:
    if x%divid==0:
        x=x/divid
        if divid not in factors:#aynı asal çarpanları tekrar yazmasının engellemek için listeye aldık
            factors.append(divid)

    else:
        divid+=1
