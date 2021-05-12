from flask import Flask,make_response,jsonify,request,render_template

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

stores = {
    'id': 'cain',
    'email': 'cain-fake@gmail.com',
    'mobile': '0912345678',
    'postition': {
        'title':'SRE',
        'departiment':'IT'
    }
}

@app.route('/', methods=["GET"])
def home():
    return "<h1>Hello World!!</h1>"

@app.route('/store', methods=["GET"])
def get_stores():
    return jsonify(stores)

app.run(host="0.0.0.0", port=8888)
