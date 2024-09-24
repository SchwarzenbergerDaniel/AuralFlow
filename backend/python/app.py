from flask import Flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/8d', methods=['GET'])
def get_hello():
    name = request.args.get("name")  # Default to "Guest" if name is not provided
    return f'<h1>Hello, {name}!</h1>'  # Use an f-string to format the response

if __name__ == '__main__':   
    app.run(debug=True)
