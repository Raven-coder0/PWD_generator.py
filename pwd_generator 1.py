import random
import string

pwd_length = int(input("Enter the 'PASSWORD' length : "))

characters = list(string.ascii_letters+string.digits+string.punctuation)

password = []

for i in range(pwd_length):
     randomchar = random.choice(characters)
    
     random.shuffle(randomchar)

password.append(randomchar)

print("the password is :"+''.join(password))
