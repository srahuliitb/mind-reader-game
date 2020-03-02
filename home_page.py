from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        'score': 'Computer score',
        'content': 'Computer scored 50 points.',
        'author': 'Rahul'
    },
    {
        'score': 'Player score',
        'content': 'Player scored 100 points.'
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)