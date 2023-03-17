from flask import flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

if __name__ == '__name__':
    app.run(debug=True, port=os.getenv('PORT'))