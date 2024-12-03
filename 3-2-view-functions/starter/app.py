from flask import Flask

app = Flask(__name__)

# some posts to simulate some data (eg. could be database data)
posts = {
    1: {'title': 'Introduction to Flask', 'content': 'Flask is a lightweight WSGI web application framework...'},
    2: {'title': 'Understanding Routes in Flask', 'content': 'Routes are a fundamental concept in Flask...'}
}

@app.route('/')
def home():
    return '<h1>Welcome to My Blog</h1><p>Click on the posts to learn more about Flask.</p>'

# Our route for displaying the posts. When the "/post/1" path is reached:
# Its view function runs getting this data for the post with key 1 and display the post's values
@app.route('/post/1')
def show_post():
    post = post[1]
    return f"<h1>{ post['title'] }</h1> <p>{ post['content'] }</p>"

if __name__ == '__main__':
    app.run(debug=True)
