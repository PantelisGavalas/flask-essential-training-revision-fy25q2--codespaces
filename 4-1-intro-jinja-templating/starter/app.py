from turtle import title
from flask import Flask, render_template

app = Flask(__name__)

'''
**  We have the render_template function we have seen to render an HTML file.
**  We can also pass arguments to it to be used in the template for dynamic content.
**  When render_template is called, it sends the data from the view function to the 
    template where it can be used to generate content.
'''
@app.route('/')
def home():
    user = {'username': 'Pantelis'}
    return render_template('index.html', title='Home', user=user)

if __name__ == '__main__':
    app.run(debug=True)
