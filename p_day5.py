import random 
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol=['!','#','$','%','&','(',')','*','+']

# easy (no reshuffle of the list)

# passcode=""
# print("Welcome to the Pypassword Genertor")
# nr_letter=int(input("how many letters you want in your password\n"))
# nr_number=int(input("how many number you want in your password\n"))
# nr_symbol=int(input("how many symbol you want in your password\n"))

# for i in range(1,nr_letter+1):
#     ran_letter=random.choice(letters)
#     passcode+=ran_letter
    
# for i in range(1,nr_number+1):
#     ran_number=random.choice(number)
#     passcode+=ran_number
    
# for i in range(1,nr_symbol+1):
#     ran_symbol=random.choice(symbol)
#     passcode+=ran_symbol
    
# print(f"your strong password is = {passcode}")



#  hard(reshuffle the list )

password=[]
print("Welcome to the Pypassword Genertor")
nr_letter=int(input("how many letters you want in your password\n"))
nr_number=int(input("how many number you want in your password\n"))
nr_symbol=int(input("how many symbol you want in your password\n"))
total=nr_letter+nr_number+nr_symbol

for i in range(1,nr_letter+1):
    ran_letter=random.choice(letters)
    password.append(ran_letter)
    
for i in range(1,nr_number+1):
    ran_number=random.choice(number)
    password.append(ran_number)
    
for i in range(1,nr_symbol+1):
    ran_symbol=random.choice(symbol)
    password.append(ran_symbol)

print(password)
random.shuffle(password)
print(password)
passcode=""
for char in password:
    passcode+=char
print(f"your strong password is = {passcode}")