
# =====================================================WHAT WE COVER=========================================================

# HTML TEMPLATES AND DYNAMIC URLS FOR THE SPECIFIC POINT ENDS 
# HOW TO USE GINGER 2 TEMPLATE ENGINE
# HOW TO CREATE THE CUSTOM FILTERS

# ==============================================================================================================================


from flask import Flask, render_template, redirect, url_for

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

@app.route("/other")
def other():
    some_text = "Hello this for the filters in flask"
    return render_template("other.html", some_text = some_text)


# revese string

@app.template_filter("reverse_string")
def reverse_string(some_text): # sometext
    return some_text[::-1]


# repeat

@app.template_filter("repeat_filter")
def repeat_filter(some_text, times = 10):
    return some_text * times
                     
# alternative upper and lower

@app.template_filter("alternate_case")
def alternate_case(s): # somet_txet
    result = []
    for index, c in enumerate(s):
        if index % 2 == 0:
            result.append(c.upper())
        else:
            result.append(c.lower())

    return "".join(result)
            
# REDIRECT IMPORT REDURECT FUNCTION
# URL_FOR FOR REDIRECT
# While typing in the url of Front end

@app.route("/redirect_endpoint")
def redirect_endpoint():
    return redirect(url_for("other"))


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)