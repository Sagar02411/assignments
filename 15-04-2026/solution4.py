import os
dir = "C:\Users\Thinkbiz\OneDrive - VeBuIn\Desktop\Assignments_practice\assignments"
for file in os.listdir(dir):
    if file.endswith(".txt"):
        print(os.path.join(dir, file))