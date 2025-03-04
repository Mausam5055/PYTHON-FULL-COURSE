# 7. Explore the ‘Flask’ module and create a web server using Flask & 
# Python. 
  
from flask import Flask    

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Mausam,what are u doing!</p>"

app.run()


#if we click in the server from the link given the terminal then we will
#see our "hello world" printd in the web sever


#NOTES: 1.app = Flask(__name__): This line creates a new Flask web 
# application and stores it in the variable app. You'll use app to 
# configure the application, define routes, and start the server.
#In short, app = Flask(__name__) sets up the foundation for your 
# Flask web app, giving you a starting point to build upon.

# 2. @app.route("/"): This is a decorator in Python. It tells 
# Flask that the function directly below it (in this case, hello_world) should run whenever someone 
# visits the URL path / (the homepage of the website). 
# The "/" represents the root of your website, 
# like www.example.com/.

#3. def hello_world():: This defines a function in Python 
# named hello_world. This function contains the code that 
# will be executed when the route is accessed.   


                # Putting it all together:
                # @app.route("/")
                # def hello_world():
                #     return "Hello, World!

# 4.When someone visits the homepage of your web app, 
# the hello_world function is triggered, and the browser 
# displays the text "Hello, World!" as a response.So, 
# this code sets up the simplest possible web page using 
# Flask, where visiting the root URL shows the message 
# "Hello, World!".
