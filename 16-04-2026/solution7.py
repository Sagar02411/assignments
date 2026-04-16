# --------------------------------------------------
# Q7: Complete the Function
# Return a dictionary with character frequency.
# Example: "aab" -> {'a':2, 'b':1}
# --------------------------------------------------
from collections import Counter

def char_frequency(s):
    return Counter(s)



print(char_frequency("aaad"))