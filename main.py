from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello world</h1><a href="/new?value=jack"><button>Go to new page</button></a>'

@app.route('/new')
def new():
    value_passed = request.args.get('value')
    return f'<h2>Hai, I am new</h2><p>I am : {value_passed} </p><a href="/"><button> go to home page</button></a>'

app.run()