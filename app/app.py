from flask import Flask
from flask_cors import CORS



app = Flask(__name__)
app.config['SECRET_KEY']='Th1s1ss3cr3t'
CORS(app)
