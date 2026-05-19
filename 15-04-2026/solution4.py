# Q4 (Medium) – os Library
    
# import os
# contents = os.listdir()
# print("Current directory contents:", contents)


import os

# Path to the directory (absolute or relative)
dir = r"C:\Users\Thinkbiz\OneDrive - VeBuIn\Desktop\Assignmnets"

# os.listdir return a list of all files within 
# the specified directory
for file in os.listdir(dir):

        # The following condition checks whether 
    # the filename ends with .txt or not
    if file.endswith(".txt"):

        # Appending the filename to the path to obtain 
        # the fullpath of the file
        print(os.path.join(dir, file))