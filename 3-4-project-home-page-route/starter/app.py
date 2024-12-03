from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Home Page route that renders our index.html
'''
** render_template: function provided by flask
** It allows us to render HTML templates.
** Combines the template with our data and returns final HTML content.
** By default looks for the specified file in the templates folder.
'''
@app.route('/')
def index():
    return render_template('index.html')

# Form route where user inputs data
'''
** We have both POST and GET methods declared in our methods=[] list in the route.
** We get the method via the request object (request.method) which we import at the top.
    --> request: used to handle HTTP requests. It contains all the data sent from client to server.
** We also import redirect and url_for with which we redirect the user to the url_for the dashboard
    --> redirect: sends a redirect responce to the client.
    --> url_for: used to build a URL to the given endpoint with the method provided.
'''
@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        #process form data here
        return redirect(url_for('dashboard'))
    return render_template('form.html')

# Dashboard page route that renders our dashboard.html
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
