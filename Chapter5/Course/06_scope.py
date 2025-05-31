def test():
    # variable local
    num = 100
    print(num)

# variable global
num = 100
def test_a():
    print(num)

def test_b():
    print(num)

test_a()
test_b()
