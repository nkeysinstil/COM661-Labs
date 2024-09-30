from flask import Flask, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return make_response("<h1>Hello World r</h1>", 200) # HTTP 200 meaning success

@app.route('/com661', methods=['GET'])
def com661():
    return make_response("<h1>Welcome to COM661</h1>", 200) # HTTP 200 meaning success

@app.route('/module/<string:code>', methods=['GET'])
def module(code):
    return make_response("<h1>Welcome to " + code.upper() + "</h1>", 200) # HTTP 200 meaning success

if __name__ == '__main__':
    app.run(debug=True, port=3000)