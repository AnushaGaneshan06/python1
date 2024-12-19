# Simple application

from flask import Flask

app = Flask(__name__) # 1. create application

# 2. decorator @app and route
# ------------------------

@app.route('/')
# 3. Function that to return something
def index():
    return "<h1>Hello world!!</h1>"



# ANOTHER METHOD 
@app.route("/hello")  
 # Function to handle GET requests to the root path "/"
def index2():
    return "Hi this the python flask framework apllication"




if __name__ == "__main__":
    # 3 paramter we can provide here is host port or (debug mode or not)
    # Always run the application in the local host
    # (0.0.0.0) is the local IP ADDRESS
    # Debug is for we dont need to retart the code again and again.

    app.run(host = "0.0.0.0", port = 44444, debug = True)
    
# ---------------PORT MECHANISM---------------
# PORT 4444 IS THE USER DEFINED NUMBER , WHERE WE CAN RUN IN LOCAL HOST & WORKS ON PRIVATE IP ADDRESS 
 
#  * Running on all addresses (0.0.0.0) => port
#  * Running on http://127.0.0.1:44444 => local host
#  * Running on http://192.168.29.44:44444 => private ip address

# -----------NORMAL--------
    # app.run(host = "0.0.0.0", debug = True) 
    # its common ip address with 5000 has port number
