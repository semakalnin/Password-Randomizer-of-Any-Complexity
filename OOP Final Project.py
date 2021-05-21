import random

user = input("How hard do you want your password to be? ")
user = user.lower()
password_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
password = []
password2 = []
password3 = []

#Defining function to generate passwords
def password_generater(**kwargs):
    for i in range (lengs):
        password.append(random.choice(password_characters))
    for j in range (lengs2):    
        password2.append(random.choice(password_characters))
    for k in range (lengs3):
        password3.append(random.choice(password_characters))
    printer()

#Defining fuction to print passwords
def printer():    
    print("".join(password))
    print("".join(password2))
    print("".join(password3))

#Range of password difficulties
if user in ("easy", "легкий", "простой","Easy"):
    lengs = random.randint(4,5)
    lengs2 = random.randint(5,6)
    lengs3 = random.randint(6,7)
    password_generater()

elif user in ("medium", "средний", "нормальный","Medium"):
    lengs = random.randint(8,9)
    lengs2 = random.randint(9,10)
    lengs3 = random.randint(11,12)
    password_generater()

elif user in ("hard", "сложный","Hard"):
    lengs = random.randint(13,14)
    lengs2 = random.randint(15,16)
    lengs3 = random.randint(17,18)
    password_generater()

elif user in ("4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"):
    lengs = int(user)
    lengs2 = int(user)
    lengs3 = int(user)
    password_generater()

elif user in ("1","2","3"):
    print("Password is too short")

elif user in ("19","20","21","22","23","24","25","26","27","28","29","30"):
    print("Password is too long")

#If user input out of range
else:
    print("I don't understand.")
