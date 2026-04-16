# Q5 (Medium) – random Library
import random
import string

def generate_password(length):
    # Generate random password using letters and digits
    # store all characters in lists 
    
    
    s1 = list(string.ascii_lowercase)
    s2 = list(string.digits)
    # check this input is it number? is it more than 8?
    # while length > 0:

    characters_number = int(length)

    # shuffle all lists
    random.shuffle(s1)
    random.shuffle(s2)


    # calculate 50% & 50% of number of characters
    part1 = round(characters_number * (50/100))
    part2 = round(characters_number * (50/100))

    result = []

    for x in range(part1):

        result.append(s1[x])

    for x in range(part2):
        result.append(s2[x])

    # shuffle result
    random.shuffle(result)

    # join result
    password = "".join(result)
    print(password)

generate_password(8)