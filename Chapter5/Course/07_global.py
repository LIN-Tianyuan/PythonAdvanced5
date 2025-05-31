"""
num = 100

def test_a():
    print(num)

def test_b():
    num = 200
    print(num)

test_a()    # 100
test_b()    # 200
print(num)  # 100
"""

num = 100

def test_a():
    print(num)

def test_b():
    global num
    num = 200
    print(num)

test_a()    # 100
test_b()    # 200
print(num)  # 200