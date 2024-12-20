from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id":1, "title":"Book1", "author" : "Author1"},
    {"id":2, "title":"Book2", "author" : "Author2"},
    {"id":3, "title":"Book3", "author" : "Author3"}
]

# get all books 

@app.route("/books", methods=[  "GET"])
def get_books():
    return books

# get specific book 
@app.route("/books/<int:book_id>", methods = ["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
        
    return {"error" : "book not found"}


# create book
@app.route("/books/",methods = ["POST"])
def create_book():
    new_book = {"id":len(books) + 1, "title" : request.json["title"], "author": request.json["author"]}
    books.append(new_book)
    return new_book

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)