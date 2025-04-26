a = 1
while a < 10:
    b = 1
    while b <= a:
        print(f"{a} x {b} = {a*b}", end="\t")
        b += 1
    print()
    a += 1