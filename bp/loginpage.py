from flask import Flask,request,jsonify, Blueprint
from flask_mail import Mail, Message
# from app import app
from flask import current_app
import random
import string 
from datetime import datetime, timedelta
import re
# from common_utils.logging_utils import setup_logger
# from flask_cors import CORS
from config import  LoginConfig, UserConfig

login_bp = Blueprint('login', __name__, url_prefix='/login')

# current_app = Flask(__name__)
# CORS(login_bp)

# logger= setup_logger()
mail= Mail()

collection = UserConfig.get_users_collection()

# @login_bp.route("/")
# def index():
#   current_
#   current_
#   current_
#   current_
#   current_
#   mail.init_app(current_app)
#   return "Login Blueprint Index"

 

def generate_otp():
    otp = ''.join(random.choices(string.digits, k=6))
    otp_timestamp= datetime.now()
    return otp, otp_timestamp

def is_valid_email(email):
    regex=r'^[a-zA_Z0-9_.+-]+@[a-zA-Z0-9_]+\.[a-zA_Z0-9_.]{2,}$'
    return bool(re.match(regex,email))

otp_storage={}

# @login_bp.route('/send_otp', methods=['POST'])
# def send_otp():
#     """
#     Endpoint to send OTP to the provided email address.

#     ---
#     parameters:
#       - in: body
#         name: email
#         description: The email address where the OTP will be sent.
#         required: true
#         schema:
#           type: object
#           properties:
#             email:
#               type: string
#     responses:
#       200:
#         description: A Message indicating that the OTP has been sent successfully.
#       400:
#         description: Invalid email address provided.
#       500:
#         description: Internal server error occurred.
#     """
#     try:
#         data = request.get_json()
#         recipient = data.get('email')
        
#         if not is_valid_email(recipient):
#             return jsonify({'error': 'Invalid email address provided'}), 400
        
#         msg = Message('Your OTP', sender='aapmorblogs@gmail.com', recipients=[recipient])

#         otp, otp_timestamp = generate_otp()

#         collection = LoginConfig.get_login_details()

#         result = collection.insert_one({'email': recipient, 'otp': otp, 'timestamp': otp_timestamp})

#         if result.inserted_id:
#             msg.body = f'Your OTP is: {otp}'
#             mail.send(msg)
#             return jsonify({'message': 'OTP sent successfully', 'otp': otp})
#         else:
#             return jsonify({'error': 'Failed to insert OTP data into MongoDB'}), 500
#     except Exception as e:
#         return jsonify({'error': 'Internal server error occurred'}), 500


@login_bp.route('/send_otp', methods=['POST'])
def send_otp():
    """
    Endpoint to send OTP to the provided email address.

    ---
    parameters:
      - in: body
        name: email
        description: The email address where the OTP will be sent.
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
    responses:
      200:
        description: A Message indicating that the OTP has been sent successfully.
      400:
        description: Invalid email address provided.
      500:
        description: Internal server error occurred.
    """
    try:
        data = request.get_json()
        recipient = data.get('email')
        
        if not is_valid_email(recipient):
            # logger.error('Invalid email address provided: %s', recipient)
            return jsonify({'error': 'Invalid email address provided'}), 400
        
        msg = Message('Your OTP', sender='aapmorblogs@gmail.com', recipients=[recipient])

        otp, otp_timestamp = generate_otp()
        

        collection = LoginConfig.get_login_details()

        with current_app.app_context():
        # Insert data into MongoDB collection
          result = collection.insert_one({'email': recipient, 'otp': otp, 'timestamp': otp_timestamp})

          if result.inserted_id:
              msg.body = f'Your OTP is: {otp}'
              mail.send(msg)
              # logger.info('OTP sent successfully to %s', recipient)
              return jsonify({'message': 'OTP sent successfully', 'otp': otp})
          else:
              # logger.error('Failed to insert OTP data into MongoDB')
              return jsonify({'error': 'Failed to insert OTP data into MongoDB'}), 500
    except Exception as e:
        # logger.error('Error sending OTP: %s', str(e), exc_info=True)
        return jsonify({'error': 'Internal server error occurred'}), 500

    
@login_bp.route('/verify_otp', methods=['POST'])
def verify_otp():
    """
    Endpoint to verify the OTP provided by the user.

    ---
    parameters:
      - in: body
        name: otp
        description: The OTP received by the user.
        required: true
        schema:
          type: object
          properties:
            email:
              type: string  # Adding email as a parameter
            otp:
              type: string
    responses:
      200:
        description: A message indicating successful OTP verification.
      400:
        description: Invalid OTP provided or OTP expired.
      500:
        description: Internal server error occurred.
    """
    try:
        data = request.get_json()
        otp_received = data.get('otp')
        email = data.get('email')
          

        collection = LoginConfig.get_login_details()
        logindata = collection.find_one({'email': email,"otp":otp_received})
        

        if not logindata:
            # logger.warning('Email not found in login details: %s', email)
            return jsonify({'error': 'Invaild OTP'}), 400

        correct_otp = logindata['otp']
        correct_otp_timestamp = logindata['timestamp']
        

        if datetime.now() - correct_otp_timestamp > timedelta(minutes=2):
            # logger.warning('OTP verification failed: OTP expired for %s', correct_otp)
            return jsonify({'error': 'OTP expired. Please request a new one.'}), 400

        if otp_received == correct_otp:
            # logger.info('OTP verification successful for %s', correct_otp)
            
            # You may want to delete the OTP data from MongoDB after successful verification
            # collection.delete_one({'email': email})

            return jsonify({'message': 'OTP verification successful. Login successful!', 'email': email})
        else:
            # logger.warning('Invalid OTP provided: %s', otp_received)
            return jsonify({'error': 'Invalid OTP'}), 400
    except Exception as e:
        # logger.error('Internal server error occurred: %s', str(e), exc_info=True)
        return jsonify({'error': 'Internal server error occurred'}), 500


if __name__ == '__main__':
    mail.init_app(current_app)
