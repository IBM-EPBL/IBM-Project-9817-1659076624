from flask import Flask, render_template, session, redirect
import pymongo

app = Flask(__name__)

# Database
# client = pymongo.MongoClient('localhost', 27017)
client = pymongo.MongoClient("mongodb+srv://admin-Vaishnavi:test1234@cluster0.cghftwz.mongodb.net/?retryWrites=true&w=majority")
db = client.ckdPatientDB
# collection = db.patients
# Routes
from user import routes

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/details/')
def details():
  users = db.patients.find()
  return render_template('details.html', users = users)