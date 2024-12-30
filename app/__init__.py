from flask import Flask

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'temporary_secret_key'

# Import routes after app initialization
from app import routes
