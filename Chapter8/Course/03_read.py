count = 0

for line in open("word.txt", "r"):
    print(line)
    if "alex" in line:
        count += 1

print(count)