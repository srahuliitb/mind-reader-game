from flask import Flask

app = Flask(__name__)


@app.route('/flask')
def hello_flask():
    return "Hello, Flask"


@app.route('/rahul')
def hello_rahul():
    return "Hello, Rahul"


if __name__ == "__main__":
    app.run(debug=True)
