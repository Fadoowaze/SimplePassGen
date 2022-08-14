import os.path, random
from art import *

def pass_gen():
    aprint("bearhug")
    global password
    password = ''
    for x in range(int(input('len pass'+ "\n"))): 
        password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ+-/*!&$#?=@<>'))
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

def main():
    tprint("SimplePassGen")
    aprint("acid")
    print("site name")
    global site
    site = input()
    email_gen()
    pass_gen()
    write_in_file()

if __name__ == "__main__":
    main()

    
