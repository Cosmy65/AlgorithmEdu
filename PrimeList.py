
primeNumbers = []
for x in range(2, 10):
    div = 2
    control = 0#2 bir alttaki döngüye giremedi zaten,kontrol noktası sayesinde listeye eklendi
    while div < x:
        if x % div == 0:
            control = 1
            break  # bölen bulunduysa çık
        div += 1

    if control == 0:
        primeNumbers.append(x)

print(primeNumbers)
