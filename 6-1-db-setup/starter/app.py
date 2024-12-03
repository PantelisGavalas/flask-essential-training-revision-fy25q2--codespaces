from flask import Flask, render_template, request
from forms import MyForm
# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

# app configurations for the database URI (track modifications --> false for performance reasons)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initialize SQLAlchemy with our app 
db = SQLAlchemy(app)

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        return render_template('success.html', username=username, email=email)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

