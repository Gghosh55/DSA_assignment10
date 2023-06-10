def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]  # Swap characters
            permute(s, l + 1, r)  # Recursively permute the remaining characters
            s[l], s[i] = s[i], s[l]  # Revert the swap


# Test the function
str = "cd"
n = len(str)
permute(list(str), 0, n - 1)
