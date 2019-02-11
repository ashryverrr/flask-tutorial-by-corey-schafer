from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm 
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
   return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
       flash(f'Account Created for {form.username.data}!', 'success')
       return redirect(url_for('home'))
   else:    
       return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
       flash(f'Account Created for {form.username.data}!', 'success')
       return redirect(url_for('home'))
   else:    
       return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.secret_key='f0cd1d10ae8db07ee1b87c865b656329'
    app.run(debug = True)