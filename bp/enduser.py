from flask import Flask, jsonify, Blueprint
# from config import UserConfig
# from common_utils.logging_utils import setup_logger

app = Flask(__name__)

# logger = setup_logger()

enduser_bp = Blueprint('enduser', __name__, url_prefix='/api/v1/enduser')


# collection = UserConfig.get_users_collection()

@enduser_bp.route('/get', methods=['GET'])
def get_enduser_data():
    try:
      return "EndUser Get Request", 200
    except Exception as e:
      # logger.error('Error occurred while retrieving end user data: %s', str(e))
      return jsonify({'error': str(e)}), 500
