def stringLength(s):
    if s == '':
        return 0
    else:
        return 1 + stringLength(s[1:])


print(stringLength("abcd"))
print(stringLength("GEEKSFORGEEKS"))
