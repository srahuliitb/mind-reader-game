from flask import Flask

app = Flask(__name__)


@app.route('/getOnly')
def get_only(methods=['GET']):
    return "Only get method is allowed."


@app.route('/postOnly')
def post_only(methods=['POST']):
    return "Only post method is allowed."


@app.route('/getAndPost')
def get_and_post():
    return "Both the get and post methods are allowed."


if __name__ == "__main__":
    app.run(debug=True)
