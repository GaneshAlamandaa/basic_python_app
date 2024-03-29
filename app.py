from flask import Flask
from bp.enduser import enduser_bp


app = Flask(__name__)



app.register_blueprint(enduser_bp)

@app.route('/') 
def hello_world(): 
    return 'Hello Ramagopal Krishna!'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")