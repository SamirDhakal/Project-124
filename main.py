from flask import Flask,jsonify, request

app = Flask(__name__)

data = [
    {
        'id': 1,
        'contact': '8374928374',
        'name': 'Bob', 
        'done': False
    },
    {
        'id': 2,
        'contact': '0123819748',
        'name': 'Bill', 
        'done': False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': data[-1]['id'] + 1,
        'Contact': request.json['Contact', ""],
        'name': request.json.get('name'),
        'done': False
    }
    
    data.append(contact)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
