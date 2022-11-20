from flask import Flask
from app import app
from user.models import User

@app.route('/user/patient', methods=['POST', 'GET'])
def patient():
  return User().patient()