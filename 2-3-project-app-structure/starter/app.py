# import the Flask class from the flask module
# and create an instance of it
# __name__: built-in Python variable that gets the current module name
# It is used to tell Flask where to look for resources (templates, static files etc).
from flask import Flask, render_template
app = Flask(__name__)

# Decorator to define homepage route ("/") and index() view function, 
# to be triggered on this routeURL, where we render our html page.
@app.route("/")
def index():
  return render_template("index.html")

#run the app in debug mode
# Ensures that our Flask app runs only if the script is 
# executed directly (not when imported as a module).
if __name__ == "__main__":
  app.run(debug=True)