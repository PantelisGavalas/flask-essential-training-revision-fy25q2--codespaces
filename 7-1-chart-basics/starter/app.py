from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Chart.js Example!"

# We create a route to render the chart.html template
@app.route('/chart')
def chart():
    return render_template('chart.html')

if __name__ == '__main__':
    app.run(debug=True)
