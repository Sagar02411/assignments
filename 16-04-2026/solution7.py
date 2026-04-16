def char_frequency(s):
    freq = {}
    for c in s:
        if c in freq:
            freq[c]+=1
        else:
            freq[c]=1
    return freq
print(char_frequency('abcd'))
   
        
# --------------------------------------------------
# Q7: Complete the Function
# Return a dictionary with character frequency.
# Example: "aab" -> {'a':2, 'b':1}
# -------------------------------------------------