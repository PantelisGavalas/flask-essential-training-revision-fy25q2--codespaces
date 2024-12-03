from flask import Flask, render_template, request
from forms import MyForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    # Checks if form was submitted with POST request and if all form data is valid based on validators we've defined.
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        return f"Hello, {username}! We've received your email: {email}"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
