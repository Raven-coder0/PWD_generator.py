import random
import string

Pwd_len = int(input("Enter the length of the password: "))
print()
character_list = []
print("""_____________________ Character Sets__________________
      
      characters = '1'  | character & number  = '1,2'
      Digits     = '2'  | character & symbols = '1,3'
      Symbols    = '3'  | nuumbers & symbols  = '2,3'
                        | For All             = '1,2,3'
______________________________________________________
    """)

characterset = (input("Select the charater sets from above options: "))

if characterset == "1":
    character_list+= string.ascii_letters

elif characterset == "2":
    character_list+= string.digits  

elif characterset == "3":
    character_list+= string.punctuation

elif characterset == "1,2":
    character_list+= string.ascii_letters+string.digits

elif characterset == "1,2,3":
    character_list+= string.punctuation+string.ascii_letters+string.digits

elif characterset == "1,3":
    character_list+= string.ascii_letters+string.punctuation     

elif characterset == "2,3":
    character_list+= string.punctuation+string.digits
elif characterset == "":
    print ("invalid input")     
    quit()

password = []
for i in range (Pwd_len):
    randomchar = random.choice(character_list)
    password.append(randomchar)
    random.shuffle(password)

print()
print("THE PASSWORD IS "+"".join(password))
print()
print("_._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._.")