import os.path
import random
from art import *


def pass_gen():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    aprint("bearhug")
    length = int(input('len pass'+ "\n"))
    global password
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password
    
def email_gen():    
    global email
    a = random.randrange(len("email"))
    email = list("wizzyshadowzz")
    email.insert(a, ".")
    email = ''.join(email) + "@gmail.com"
    return email

def write_in_file():
    global site
    global email
    global password
    if os.path.exists("password.txt") == True:
        file = open("password.txt", "a")
        file.write(str(site) + "\n")
        file.write(str(email) + "\n")
        file.write(str(password) + "\n")
        file.write(" " + "\n")
        file.close()
    else:
        file = open("password.txt", "w")
        file.write(str(site) + "\n")
        file.write(str(email) + "\n")
        file.write(str(password) + "\n")
        file.write(" " + "\n")

def print_m_p():
    global email
    global password
    print(email)
    print(password) 


def main():
    tprint("SimplePassGen")
    aprint("acid")
    print("site name")
    global site
    site = input()
    email_gen()
    pass_gen()
    print_m_p
    write_in_file()

if __name__ == "__main__":
    main()