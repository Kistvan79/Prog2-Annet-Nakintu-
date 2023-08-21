
try:
    line = input("Input your integers --> ")
    a, b = line.split()
    a = int(a)
    b = int(b)
    while 0 <= a <= 1000000 and 0 <= b <= 1000000:
        if a > b:
            print(b, a)
            break
        elif b < a:
            print(a, b)
            break

except ValueError:
    print("Please input 2 integers from 0 to 1 000 000")
   