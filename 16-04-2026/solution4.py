# --------------------------------------------------
# Q4: Debug the Code
# The function should reverse a string.
# --------------------------------------------------

def reverse_string(s):
    rev = ""
    for i in range(1, len(s) + 1):
        rev += s[len(s) - i]   
    return rev

print(reverse_string("hell"))
