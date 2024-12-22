
# speacial variable shows
print(dir())

# DIRECTLY RUNS SHOWS __MAIN__
print(__name__)  

# ---------------------------------------------

print("This the main function where the __name__ return the name : ")

def display(name):
    return name

def do_something():
    print("function")



# NOW WE SET THE if CONDITION OF  NAME == MAIN HERE 
# THEN HERE WHEN WE IMPORT MAIN.PY TO  MODULE THERE THE MAIN CONDITION FAILED AND THE UNDER MAIN WILL NOT WORKDED

# ONLY 0 INDENTATION WILL WORK IN MODULE 
if __name__ == "__main__":
    print("main file : ")
    name = input("enter the name : ")
    print(display(name))
    do_something()

# Secure these fn from importing