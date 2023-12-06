##Uppgift 2 Alltså... den gör sitt jobb...Ish
N = int(input())
counter = -1
for a in range(N):
    produkt = a*(a+1)*(a+2)
    if produkt not in range(N):
        print(counter)
        break
    counter += 1