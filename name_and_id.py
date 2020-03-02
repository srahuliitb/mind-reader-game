from flask import Flask

app = Flask(__name__)


@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name, id):
    return "Hello, {}! Your id is {}".format(name.title(), id)


if __name__ == "__main__":
    app.run(debug=True)