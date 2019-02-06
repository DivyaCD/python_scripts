from flask import Flask, jsonify, abort, make_response

app=Flask("__name__")

@app.route('/')
def index():
    return "Hello, World!"

categoryDetails = [
    {
        "itemID": "Abc",
        "R2D2": "aaa",
        "RHID": "bbb",
        "Email": "abc@gmail.com"
    },
    {
        "itemID": "Cde",
        "R2D2": "ccc",
        "RHID": "ddd",
        "Email": "cde@gmail.com"
    },
    {
        "itemID": "Fgh",
        "R2D2": "fff",
        "RHID": "ggg",
        "Email": "Fgh@gmail.com"
    }
]

@app.route('/todo/api/v1.0/categoryDetails', methods=['GET'])
def get_categoryDetails():
    return jsonify({'Category Details': categoryDetails})

@app.route('/todo/api/v1.0/categoryDetail/<string:input_itemID>', methods=['GET'])
def get_categoryDetail(input_itemID):
    for categoryDetail in categoryDetails:
        if(categoryDetail['itemID'] == input_itemID):
            return jsonify({'Category Detail': categoryDetail})
    abort(404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
