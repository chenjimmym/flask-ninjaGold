from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'aSecret'

@app.route('/')
def start():
    session['goldAmount']
    return render_template('index.html')
@app.route('/processMoney', methods=['POST'])
def getMoney():
    print "hello"
    if request.form['building'] == 'farm':
        session['goldAmount'] += random.randrange(10,21)
    elif request.form['building'] == 'cave':
        session['goldAmount'] += random.randrange(5,11)
    elif request.form['building'] == 'house':
        session['goldAmount'] += random.randrange(2,6)
    elif request.form['building'] == 'casino':
        session['goldAmount'] += random.randrange(-50,51)
    else:
        session['goldAmount'] = 0
    return redirect('/')

app.run(debug=True)