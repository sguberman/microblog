from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Seth'}  # fake user
    posts = [  # fake array of posts
             {
                 'author': {'nickname': 'John'},
                 'body': 'Beautiful day in Jersey!'
             },
             {
                 'author': {'nickname': 'Susan'},
                 'body': 'The Avengers movie was pretty good.'
             }
            ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
