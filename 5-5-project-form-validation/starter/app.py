from flask import Flask, render_template, request, redirect, url_for
from forms import HealthDataForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = HealthDataForm()
    if form.validate_on_submit():
        # Process form data here
        # We retrieve the data submitted from the form to store in the database later
        date = form.date.data
        exercise = form.exercise.data
        meditation = form.meditation.data
        sleep = form.sleep.data
        # Redirect to the dashboard
        return redirect(url_for('dashboard'))
    return render_template('form.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)