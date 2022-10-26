from calendar import c
from lib2to3.pgen2 import token
from flask import Flask, render_template, request


app = Flask(__name__)
acceptable_combos = {'user1':{'email': 'user@gmail.com', 'password':'abc'}, 'JaneDoe':{'email': 'jane@gmail.com', 'password':'123'}}

@app.route("/status")
def status():
    # to check the status
    return("The Authorisation Testing Server is up and running")


@app.route('/login')
def login_template():
    # allows login via html form
    return render_template('Login.html')


@app.route('/loggedin', methods = ['POST'])
def loggedin_template():
    # shows that successfully logged in via frontend
    usname = request.form['username']
    email = request.form['email']
    password = request.form['pwd']

    if usname in acceptable_combos:
        if email == acceptable_combos[usname]['email'] and password == acceptable_combos[usname]['password']:
            return render_template('Loggedin.html')
        else:
            return "The username and password/email don't match", 401
    else:
        return "The username doesn't exist", 401

@app.route('/logout', methods=["POST"])
def log_out():
    # simulates logout via front end
    return "successfully logged out", 200

@app.route('/loggedinAPI', methods=['POST'])
def loggedin_API_template():
    # login via api
    data = request.get_json(force=True)
    email = data['email']
    usname = data['username']
    password = data['password']

    if usname in acceptable_combos:
        if email == acceptable_combos[usname]['email'] and password == acceptable_combos[usname]['password']:
            login_token = 'logged_in'
            refresh_token = 'send_this_to_refresh'
            return {'login_token': login_token, 'refresh_token': refresh_token}
        else:
            return "The username and password/email don't match", 401
    else:
        return "The username doesn't exist", 401

@app.route("/refresh", methods=["POST"])
def refresh():
    # refresh token via api
    data = request.get_json(force=True)
    refresh_token = data['refresh_token']

    if refresh_token == 'send_this_to_refresh':
         login_token = 'logged_in'
         return {'login_token': login_token}
    else:
        return 'This refresh token is not valid', 401

@app.route('/logoutAPI', methods=["POST"])
def log_out_API():
    # simulates logout via api
    data = request.get_json(force=True)
    login_token = data['login_token']
    if login_token == 'logged_in':
        return "successfully logged out", 200
    else:
        return "Invalid login token", 401