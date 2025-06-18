"""
This program is just practice constructing RESTful API's using Python and Flask.
"""
# Import the Flask class from the flask module
from flask import Flask, make_response, request

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Hardcoded data, in lieu of an actual database
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

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

@app.route("/data")
def get_data():
    try:
        # Check if data exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {'message' : f'Data of length {len(data)} found'}
        else:
            # If data is empty, return a JSON response and error code 500
            return {'message' : 'Data is empty'}, 500
    except:
        # If data is not defined, return a JSON response and error code 404
        return {'message' : 'Data not found'}, 404

"""
For the next route, we will create a name_search method which will look for a 'q' argument in the request URL.
We will need to import request from flask for that.
"""
@app.route('/name_search')
def name_search():
    # Get the argument 'q' from the query parameters of the request
    query = request.args.get('q')

    # Check if the parameter is missing
    if query is None:
        return {'message' : 'Query parameter is missing'}

    # Check if the parameter is present but invalid
    if query.strip() == "" or query.isdigit():
        return {'message' : 'Invalid input'}

    # Iterate through the 'data' list to look for the person whose first name matches the query
    # We use the .lower method to make sure that the query is not case sensitive
    for person in data:
        if query.lower() in person['first_name'].lower():
            return person, 200
    
    # if no match is found, return a JSON response indicating a 404
    return {'message' : 'Person not found'}, 404

"""
Next will be a GET /count endpoint
"""
@app.route('/count')
def count():
    try:
        return {'data count' : len(data)}, 200
        
    except NameError:
        return {'message' : 'data not defined'}, 500

""""
Next is a GET /person/id endpoint
"""

@app.route('/person/<var_name>')
def find_by_uuid(var_name):
    for person in data:
        if person["id"] == str(var_name):
            return person
    return {'message' : 'Person not found'}, 404

"""
Next, a DELETE endpoint
"""

@app.route('/person/<var_name>', methods=['DELETE'])
def delete_person(var_name):
    for person in data:
        if person['id'] == str(var_name):
            data.remove(person)
            return {'message' : 'Person deleted'}, 200
    return {'message' : 'Person not found'}, 404

"""
Finally, a global error handler
"""
@app.errorhandler(Exception)
def handle_exception(e):
    return {'message' : str(e)}, 500