from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///posts.db'
db = SQLAlchemy(home_page)

class BlogPost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False) # This field is required. It can't be null.
	content = db.Column(db.Text, nullable=False)
	author = db.Column(db.String(20), nullable=False, default='N/A')
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return 'Blog post' + str(self.id)


all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the first post.',
        'author': 'Rahul Singh',
        'date_posted': 'February 29, 2020'
    },
    {
        'title': 'Post 2',
        'content': 'This is the second post.',
        'date_posted': 'March 3, 2020'
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    return render_template('posts.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)