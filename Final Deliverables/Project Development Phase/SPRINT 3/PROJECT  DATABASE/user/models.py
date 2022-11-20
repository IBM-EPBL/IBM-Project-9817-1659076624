
from flask import Flask, jsonify, request,session
from app import db
import uuid

class User:

  def patient(self):
    print(request.form)
    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "age": request.form.get('age'),
      "bp": request.form.get('bp'),
      "sg": request.form.get('sg'),
      "al": request.form.get('al'),
      "su": request.form.get('su'),
      "rbc": request.form.get('rbc'),
      "pc": request.form.get('pc'),
      "pcc": request.form.get('pcc'),
      "ba": request.form.get('ba'),
      "bgr": request.form.get('bgr'),
      "bu": request.form.get('bu'),
      "sc": request.form.get('sc'),
      "sod": request.form.get('sod'),
      "pot": request.form.get('pot'),
      "hemo": request.form.get('hemo'),
      "pcv": request.form.get('pcv'),
      "wc": request.form.get('wc'),
      "rc": request.form.get('rc'),
      "htm": request.form.get('htm'),
      "dm": request.form.get('dm'),
      "cad": request.form.get('cad'),
      "appet": request.form.get('appet'),
      "pe": request.form.get('pe'),
      "ane": request.form.get('ane'),
    }      
    db.patients.insert_one(user)
    return jsonify(user), 200
