import random

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = ['0','1','2','3','4','5','6','7','8','9']
syms = ['!','@','#','$','%','^','&','*','+','_']

def random_password():
    password = []
    i = 0
    while i <=2:
        char = random.randint(0,26)
        num = random.randint(0,9)
        sym = random.randint(0,9)
        password.append(chars[char])
        password.append(nums[num])
        password.append(syms[sym])
        i+=1
    print("".join(password))

random_password()

