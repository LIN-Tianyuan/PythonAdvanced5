def str_reverse(s):
    str_rev = ""
    # str_rev = str_rev + s[len(s) - 1]
    # str_rev = str_rev + s[len(s) - 2]
    # str_rev = str_rev + s[len(s) - 3]
    # str_rev = str_rev + s[0]
    # str_rev = s[0] + str_rev    # "a"
    # str_rev = s[1] + str_rev    # "la"
    # str_rev = s[2] + str_rev    # "ela"
    # ...
    # s[len(s) - 1]

    i = 0
    while i <= len(s) - 1:
        str_rev = s[i] + str_rev
        i = i + 1
    return str_rev


def substr(s, x, y):
    # Coupe la chaîne de caractères par les indices x et y
    pass

# name = "alexsss" # sssxela
name = "alex"   # xela
# print(len(name))

print(str_reverse(name))
# str_reverse("alex") -> "xela"
# substr("alex", 1, 2) -> "le"

my_list1 = [1, 2, 3, 4, 5]
# [1, 2, 3]
