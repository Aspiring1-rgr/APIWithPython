"""
This program is just practice constructing RESTful API's using Python and Flask.
"""
# Import the Flask class from the flask module
from flask import Flask, make_response

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL. This just returns a plain text response.
    return "Hello World!"

# A method that provides an explicit return status using a tuple.
@app.route("/no_content")
def no_content():
    """
    Return 'No content found' with a status of 204.
    The first part of the tuple is a dict with key 'message' and id 'No content found'
    The second part of the tuple is the appropriate error code, indicating that the request succeeded but no data needs to be returned.
    The message is ignored with error code 204. With 200 it will actually return the JSON message.

    Returns:
       string: No content found
       status code: 204
    """
    return ({'message' : 'No content found'}, 204)

# Using the make_response() method to create a full HTTP response object manually.
@app.route("/exp")
def index_explicit():
    """
    Note that the make_response() method requires you to import it from the flask module.
    """
    resp = make_response({'message' : 'Whoa, no content found here either.'})
    resp.status_code = 200
    """
    Also note, because I keep doing it for some reason, your status codes do not go in curly brackets.
    """
    return resp 