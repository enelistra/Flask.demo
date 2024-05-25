from flask import Flask, redirect,render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show',methods=['POST'])
def show():
    if request.method == 'POST':
        name = request.form['name']
        result = name
        return redirect(url_for('result',result = result))

@app.route('/result/<result>')
def result(result):
    return render_template('result.html',result=result)
if __name__ == '__main__':
    app.run(debug = True)

