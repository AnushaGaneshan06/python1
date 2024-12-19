#GET REQUEST
# ----------------
from flask import Flask, request

app = Flask(__name__)

# -----FIRST METHOD ---------
@app.route("/")
def index(): # mapp the index fn in route app
    return "<h1>Hello world </h1>"


# ---------------POST METHOD ------------
# only here get method work 
# -----------------------------
@app.route("/hello", methods = ["GET","POST"]) 
#IF DECLARE THE ONLY POST  THEN WE CANT USE METHOD
# SO DECLARE BOTH POST AND GET
def hello():
    if request.method == "GET":
        return "You made the get request\n"
    
    elif request.method == "POST":
        return "You made A POST REQUEST\n"
    
    else:
        return "you will never see this message\n"
        
    



# ----------------------------------------
# STEP 1: URL PROCESSOR

@app.route("/greet/<name>") # url parameter name

def greet(name):
    return f"hello {name}"

# ------------------------


# STEP 2:

@app.route("/add/<int:number1>/<int:number2>") 
# parameter is considered as string
# if it string it wont map it bc we define the datatype inside
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"





# STEP3:  URL METHOD
# ------------------
@app.route("/handle_url_params")

def handles_params(): # IT RETURN AS DICTIONARY
    # return str(request.args)
    if "greet" in request.args.keys() and "name" in request.args.keys():
            greet = request.args["greet"]
            name = request.args.get("name")
            return f"{greet}, {name}"

    else:
         return "some paramter missing!!"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True )





# OUTPUT SHOULD PASS IN HANDLE PARAMS:
# handle_url_params?name=anuhsa&greet=hello