#1
# using only Flask

from flask import Flask, jsonify, request 

# creating a Flask app 
app = Flask(__name__) 

@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "I am using MY LAPTOP"
        return jsonify({'data': data}) 
    

@app.route('/home/<int:num>', methods = ['GET']) 
def disp(num): 
  
    return jsonify({'data': num**2}) 
  
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 


#2
# Using flask-restful

from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 

app = Flask(__name__) 
# creating an API object 
api = Api(app) 

class Hello(Resource): 
    def get(self): 
  
        return jsonify({'message': 'hello world'}) 
    
# another resource to calculate the square of a number 
class Square(Resource): 
  
    def get(self, num): 
  
        return jsonify({'square': num**2}) 
    

# adding the defined resources along with their corresponding urls 
api.add_resource(Hello, '/') 
api.add_resource(Square, '/square/<int:num>') 
  
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 

# 3
# managing a list of books

from flask import Flask, jsonify, request

app = Flask(__name__)


# Sample data

books = [
    {"id": 1, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]


# Get all books

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# Get a specific book by ID

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is not None:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404


# Add a new book

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book), 201


# Update a book

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        data = request.json
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404


# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)

