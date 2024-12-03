import email
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        
        # create a new User instance with data we got from the form
        new_user = User(username=username, email=email)
        # add it to the db session
        db.session.add(new_user)
        # commit => save the session
        db.session.commit()
        
        return redirect(url_for('success', username=username, email=email))
    return render_template('form.html', form=form)

# Create a route to render the success.html template
'''
*** The success route retrieves the username and email from 
    the request arguments and renders the success template
'''
@app.route('/success')
def success():
    username = request.args.get('username')
    email = request.args.get('email')
    return render_template('success.html', username=username, email=email)

# Route to display all users stored in the database
@app.route('/users')
def users():
    # query the database
    all_users = User.query.all()
    # pass data to our HTML template and display them in there
    return render_template('users.html', users=all_users)

if __name__ == '__main__':
    app.run(debug=True)

