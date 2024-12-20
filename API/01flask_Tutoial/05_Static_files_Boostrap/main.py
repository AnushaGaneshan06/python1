from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")

# TO UPLOAD THE IMAGE CREATE THE STTAIC FOLDER  
@app.route("/")
def index():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)