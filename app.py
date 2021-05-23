from datetime import datetime
from uuid import uuid1
from flask import Flask, jsonify

app = Flask(__name__)

data = {}

@app.route("/generate_UUID")
def generateUUID():
    """
    This function generates a timestamp and a random uuid value
    Use the data generated to populate a python dictionary in the form #Timestamp = Key, #UUID = Value
    """
    # Use the datetime module to get timestamp
    _timestamp = datetime.now().__str__()
    
    #generate a random UUID value
    _random_UUID = uuid1().hex
    
    #populate the dict
    data[_timestamp] = _random_UUID
    
    #sort the dict to descending order, latest paid at the top
    formatted_data = dict(sorted(data.items(), reverse=True))
    
    #return a json object
    return jsonify(formatted_data)


if __name__ == "__main__":
    app.run(port=2000, debug=True)