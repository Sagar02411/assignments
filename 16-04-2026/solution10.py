
# --------------------------------------------------
# Q10: Implementation
# Write a function to check if two strings are anagrams.
# Example: "listen", "silent" -> True
# --------------------------------------------------

def are_anagrams(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(are_anagrams("listen", "silent"))