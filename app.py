from flask import Flask


app = Flask(__name__)


@app.route("/status")
def status():
    return("The Authorisation Test Plugin Flask Server is up and running")


@app.route("/login", methods=["GET"])
def login():
    resp = {}

    # ~~~~~~~~~~~~ REPLACE THIS SECTION WITH OWN RUN CODE ~~~~~~~~~~~~~~~~~~~
    login_url = "www.examples.org/login"
    login_data = {'email': '<email>', 'username':'<username>','password' : '<password>'}
    login_headers = {'Accept': 'text/plain'}
    login_params = {'email':{'type': 'email', 'description': 'This is the email used for login', 'options': [], 'default': [], 'restrictions': {}},
                    'password': {'type': 'password', 'description': 'This is your password', 'options': [], 'default': [], 'restrictions': {}},
                    'username': {'type': 'text', 'description': 'This is the username for yoru account', 'options': [], 'default': [], 'restrictions': {}}
                   }
    token_params = {'access':'access', 'refresh':'refresh'}
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    resp['login_url'] = login_url
    resp['login_data'] = login_data
    resp['login_headers'] = login_headers
    resp['login_parameters'] = login_params
    resp['token_parameters'] = token_params
    return resp

@app.route("/refresh", methods=["GET"])
def refresh():
    resp = {}

    # ~~~~~~~~~~~~ REPLACE THIS SECTION WITH OWN RUN CODE ~~~~~~~~~~~~~~~~~~~
    refresh_exists = True
    login_url = "www.examples.org/refresh"
    login_data = {'refresh':'<refresh>'}
    login_headers = {}
    refresh_token_name = 'refresh'
    token_params = {'access':"access"}
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if refresh_exists:
        resp['login_url'] = login_url
        resp['login_data'] = login_data
        resp['login_headers'] = login_headers
        resp['refresh_token_name'] = refresh_token_name
        resp['token_parameters'] = token_params
        return resp
    else:
        return 'This login does not provide refresh tokens', 503
