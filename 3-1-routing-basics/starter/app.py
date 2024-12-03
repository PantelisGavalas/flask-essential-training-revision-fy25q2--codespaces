from flask import Flask

app = Flask(__name__)

# Our decorator for the homepage route "/" and its view function -->
# the function executed when this route is reached 
@app.route('/')
def home():
    return '<h1> Welcome to the Home Page!</h1> <p> Click on the posts to learn more about Flask.</p>'

if __name__ == '__main__':
    app.run(debug=True)
