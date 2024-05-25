from flask import Flask, render_template, request
addition = Flask(__name__)

@addition.route('/')
def index():
    return render_template('add.html')

@addition.route('/add',methods=['POST'])
def add():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        sum = num1 + num2
    return render_template('add.html',sum = sum)
if __name__ == '__main__':
    addition.run(debug = True)