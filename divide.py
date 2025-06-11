threedivide=[]
fivedivide=[]
commondivide=[]
for i in range(0,101):
    if i%15==0:#önce burası kontrol edilir burayı sağlayan eleman listeye alınır diğer eliflerde gösterilmez
        commondivide.append(i)
    elif i%3==0:#kalan elemanlar diğer eliflerde kontrol edilir
        threedivide.append(i)
    elif i%5==0:#burda 15 bulunmaz mesela çünkü bir üstteki if'e vermiştik
        fivedivide.append(i)

print(f"the number divided by three={threedivide}")
print(f"the number divided by five={fivedivide}")
print(f"numbers that divide both in common={commondivide}")
