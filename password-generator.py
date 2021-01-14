import random

number = int(input("How many characters do you want? "))
lst = []

for i in range(0,number):
    letter = chr(random.randint(65, 120))
    lst.append(letter)
    
    
password = "".join(lst)
print("Your new new password:\n{}".format(password))
