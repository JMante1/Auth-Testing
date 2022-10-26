import requests

# user_data is gathered based on login_params form
def get_access_token(plugin_data, user_data):
    # Pull out required information
    login_url = plugin_data['login_url']
    login_data = plugin_data['login_data'] 
    login_headers = plugin_data['login_headers']

    # Replace parameters in data and headers
    # This could be expanded to allow partial replace
    for key in login_data:
        if key in user_data:
            login_data[key] = user_data[key]
    
    for key in login_headers:
        if key in user_data:
            login_headers[key] = user_data[key]

    # Get access token
    response = requests.post(login_url, headers=login_headers, data=login_data)
    return response.content



data = {
    "login_data": {
        "email": "<email>",
        "password": "<password>",
        "username": "<username>"
    },
    "login_headers": {
        "Accept": "text/plain"
    },
    "login_parameters": {
        "email": {
            "default": [],
            "description": "This is the email used for login",
            "options": [],
            "restrictions": {},
            "type": "email"
        },
        "password": {
            "default": [],
            "description": "This is your password",
            "options": [],
            "restrictions": {},
            "type": "password"
        },
        "username": {
            "default": [],
            "description": "This is the username for yoru account",
            "options": [],
            "restrictions": {},
            "type": "text"
        }
    },
    "login_url": "www.examples.org"
}

user_data = {"email":"test@gmail.com", "password":"123", "username":"User1"}
token = get_access_token(data, user_data)
print(token)