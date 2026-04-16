def reverse_string(s):
    stack = list(s)
    rev = ""
    for i in range(len(s)):
        rev += stack.pop()# Bug here
    return rev
print(reverse_string('abcd'))