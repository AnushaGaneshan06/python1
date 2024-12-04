# pip install cryptography
# ------------------------
#  encrypt the text module
from cryptography.fernet import Fernet 

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
write_key()'''

def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# master_pwd = input("What is the master password ? ")
# key = load_key() + master_pwd.encode()
key = load_key() 
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|", 1) 
            print("user: ", user, "| password : ",fer.decrypt(passw.encode()).decode())

# b'' => bytes string 

def add():
    name = input("Account Name : ")
    pwd = input("Password : ")

    with open('password.txt', 'a') as f:
        f.write(name + "|"+ fer.encrypt(pwd.encode()).decode() + "\n")

     


while True:
    mode = input("Would you like to add the new password or view existing ones (view, add)?, Press to q quit ").lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue