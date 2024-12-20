from flask import Flask, render_template, request, Response, send_from_directory, jsonify
import pandas as pd
import os
import uuid # random id

app = Flask(__name__, template_folder="templates")

# get request = is to get the request to display the html page
# post request = submit the form to load the post request

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        number = request.form.get("number")

        if username == "anusha" and password == "pass" and number == "1234":
            return "successfull login"
        else:
            return "Failure"
        

#end point

@app.route("/file_upload", methods = ["POST"])
def file_upload():
    file = request.files["file"] #NAME IN INDEX

    if file.content_type == "text/plain":
        return file.read().decode()
    
    elif file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or file.content_type == "application/vnd.ms-excel":
    # Process the file"
    # dataframe
        df = pd.read_excel(file)
        return df.to_html() 
        # When the response is returned to the browser, the data from the Excel file will be displayed as an HTML table.



# file download

@app.route("/convert_csv", methods = ["POST"])
def convert_csv():
    file = request.files["file"]
    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype="text/csv",
        headers={
            "Content-Disposition":"attachment ; filename = result.csv"
        }

    )

# file convert

@app.route("/convert_csv_two", methods = ["POST"])
def convert_csv_two():
    file = request.files["file"]

    df = pd.read_excel(file)

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    filename = f"{uuid.uuid4}.csv"
    df.to_csv(os.path.join("downloads", filename))

    return render_template("downlaod.html", filename=filename)

    
@app.route("/download<filename>")
def download(filename):
    return send_from_directory("download", filename, download_name = "result.csv")


# JAVASCRIPT 

@app.route("/handle_post", methods = ["POST"])
def handle_post():
    greeting = request.json["greeting"]
    name = request.json["name"]

    with open("file.text", "w") as f:
        f.write(f"{greeting}, {name}")
    return jsonify({"message" : "successfully return"})
    



if __name__ == "__main__":
    app.run(debug=True)