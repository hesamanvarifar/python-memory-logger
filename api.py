from flask import Flask
from .models import MemoryLog

app = Flask(__name__)

@app.route("/")
def get_info():
    
    return 
