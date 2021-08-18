from datetime import datetime
from uuid import uuid1
from flask import Flask, jsonify

app = Flask(__name__)

data = {} 
data_list = []

@app.route("/generate_UUID")
def generateUUID():
    """
    This function generates a timestamp and a random uuid value
    Use the data generated to populate a python dictionary in the form #Timestamp = Key, #UUID = Value
    """
    # Use the datetime module to get timestamp
    _timestamp = datetime.now().__str__()
    
    # Generate a random UUID value
    _random_UUID = uuid1().hex
    
    # Use LIFO to create a list with most recent entry first
    data_list.insert(0, {_timestamp : _random_UUID})
    
    #return a json object
    return jsonify(data_list)

if __name__ == "__main__":
    app.run(port=2000, debug=True)