# --------------------------------------------------
# Q10: Implementation
# Write a function to check if two strings are anagrams.
# Example: "listen", "silent" -> True
# --------------------------------------------------

def are_anagrams(s1, s2):
    check1 = sorted(s1)
    check2 = sorted(s2)
    if check1 == check2:
        return"Yes strings are anagram"
    else:
        return"not an anagram"
print(are_anagrams(('abcd'),('bcda')))
