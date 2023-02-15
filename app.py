from flask import Flask
from blueprints.calculator import calculator

app = Flask(__name__)
app.register_blueprint(calculator)

