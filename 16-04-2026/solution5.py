"""from math import sqrt

def Prime(n, i):  
    if i == 1 or i == 2:  
        return True
    if n % i == 0:  
        return False

    return Prime(n, i - 1)
n = 13
i = int(sqrt(n) + 1)

print(Prime(n, i))"""
def Prime(n):
    if(n<=1):
        print('No')
    else:
        for i in range(2,n-1):
            if(n%i == 0):
                print("no")
                break
            else:
                return("yes")
print(Prime(13))