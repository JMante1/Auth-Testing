# Auth-Testing
A server which is used for testing auth plugins. It allows login via a frontend or API and provides login and refresh tokens via the api. It works with the auth-test plugin found at: https://github.com/SynBioHub/Plugin-Auth-Test

# Install
## Using docker
Run `docker run --publish 8104:5000 --detach --name auth-testing synbiohub/auth-testing:snapshot`
Check it is up using localhost:8101.  

## Using Python
Run `pip install -r requirements.txt` to install the requirements. Then run `FLASK_APP=app python -m flask run`. A flask module will run at localhost:5000/.
