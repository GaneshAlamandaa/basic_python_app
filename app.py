from flask import Flask,request,jsonify
from flasgger import Swagger
from flask_mail import Mail
from flask_cors import CORS
from bp.enduser import enduser_bp
from bp.loginpage import login_bp


app = Flask(__name__)
Swagger(app)
CORS(app)

# Mails
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USE_SSL']= True
app.config['MAIL_USERNAME']='aapmorblogs@gmail.com'
app.config['MAIL_PASSWORD']='vzyolkoiczhkmixa'
mail = Mail(app)

# Blue Prints
app.register_blueprint(enduser_bp)
app.register_blueprint(login_bp)




@app.route('/') 
def hello_world(): 
    return 'Hey I working on flask!'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")