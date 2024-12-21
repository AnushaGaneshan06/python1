from flask import Flask, render_template, session, make_response

app = Flask(__name__, template_folder="templates")
# secret key for session
app.secret_key = "SOME KEY"
# cookies are stored on client side

@app.route("/")
def index():
    return render_template("index.html", message = "Index")

#  changes or seen by the user trust on the service side
@app.route("/set_data")
def set_data():
    session['name'] = "mike"
    session["other"] = "hello world" # information store in session dictionary and it will store in specific session id
    return render_template("index.html", message = "Session data set")

# DATA INTO THE MESSAGE
@app.route("/get_data")
def get_data():
    if "name" in session.keys() and "other" in session.keys():
        name= session['name']
        other = session['other']
        return render_template("index.html", message = f'NAME :{name}, other: {other} ')
    else:
        return render_template("index.html", message = "No session found")


@app.route("/clear_session")
def clear_session():
    session.clear()
    return render_template("index.html", message=" session cleared")

# cookies
@app.route("/set_cookie")
def set_cookie():
    response = make_response(render_template("index.html", messsage = "cookies set."))
    response.set_cookie("cookie_name", "cookie_value" )
    # cookie name and cookie value 
    return response



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
