from flask import Flask

app = Flask(__name__)


@app.route("/<string:name>")
def hello_name(name):
    return "Hello, " + name.title()


if __name__ == "__main__":
    app.run(debug=True)
