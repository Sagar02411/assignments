# --------------------------------------------------
# Q7: Complete the Function
# Return a dictionary with character frequency.
# Example: "aab" -> {'a':2, 'b':1}
# --------------------------------------------------
from collections import Counter

def char_frequency(s):
    freq = {}

    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    print(freq)

char_frequency("aaad")