from flask import Flask, render_template
from forms import MyForm

app = Flask(__name__)

# Required in Flask-WTF for cross site request forgery protection.
app.secret_key = "supersecterkey"

# Set up a new route for our form.
# Both POST and GET requests on our form page.
# We get our form and proceed with action on if submitted and validated condition.
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        return f"Hello, {form.name.data}"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
