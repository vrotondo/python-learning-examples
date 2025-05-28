from flask import Flask

app = Flask(__name__)

@app.route('/print/<message>')
def print_message(message):
    return f"<h1>{message}</h1>"

@app.route('/count/<int:num>')
def count(num):
    return "<br>".join(str(n) for n in range(num + 1))

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Unsupported operation", 400
    return f"<h1>{num1} {operation} {num2} = {result}</h1>"

'''
# Sample in-memory data
authors = [
    {"id": 1, "name": "Octavia Butler", "books": [
        {"id": 1, "title": "Kindred"},
        {"id": 2, "title": "Parable of the Sower"}
    ]},
    {"id": 2, "name": "Toni Morrison", "books": [
        {"id": 1, "title": "Beloved"},
        {"id": 2, "title": "Song of Solomon"}
    ]}
]

# Route: GET /authors
@app.route('/authors')
def get_authors():
    return jsonify(authors)

# Route: GET /authors/<id>
@app.route('/authors/<int:id>')
def get_author(id):
    author = next((a for a in authors if a["id"] == id), None)
    return jsonify(author) if author else ("Author not found", 404)

# Route: GET /authors/<id>/books
@app.route('/authors/<int:id>/books')
def get_author_books(id):
    author = next((a for a in authors if a["id"] == id), None)
    return jsonify(author["books"]) if author else ("Author not found", 404)

# Route: GET /authors/<author_id>/books/<book_id>
@app.route('/authors/<int:author_id>/books/<int:book_id>')
def get_author_book(author_id, book_id):
    author = next((a for a in authors if a["id"] == author_id), None)
    if not author:
        return ("Author not found", 404)
    book = next((b for b in author["books"] if b["id"] == book_id), None)
    return jsonify(book) if book else ("Book not found", 404)
    '''