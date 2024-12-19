
# =====================================================WHAT WE COVER=========================================================

# HTML TEMPLATES AND DYNAMIC URLS FOR THE SPECIFIC POINT ENDS 
# HOW TO USE GINGER 2 TEMPLATE ENGINE
# HOW TO CREATE THE CUSTOM FILTERS

# ==============================================================================================================================


from flask import Flask, render_template

app = Flask(__name__, template_folder = "templates")

@app.route("/")
def index():
    # step 1 : # feed 2 value in html
    myvalue = "PYTHON"
    myresult = 10 + 20
    mylist = [10, 30, 40, 40]
    # --------------------
    # step 2 : # TO FFED IN DEX HAVE TO PASS THE KEYWORD VALUE IN RETURN
    return render_template("index.html", myvalue = myvalue, myresult = myresult, mylist=mylist)
    #step 3 in html file




if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)