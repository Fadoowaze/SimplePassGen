import os.path, random
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
    with open("password.txt", "a") as f:
        f.write(f"""
Group:General
Title: {site}
Username: {email}
Password: {password}
Tag, Tags:
Notes: Gen by SimplePassGen
Iconid: 0
ExpiryTime: 
""")
        f.close()


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

    