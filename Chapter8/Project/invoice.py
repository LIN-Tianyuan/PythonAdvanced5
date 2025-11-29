with open("bill.txt", 'r') as f:
    with open("bill.txt.bak", "w") as bak:
        for line in f.readlines():
            if "test" not in line:
                bak.write(line)