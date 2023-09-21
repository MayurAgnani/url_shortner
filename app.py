from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
import datetime;
import redis
from flask_socketio import SocketIO, join_room, leave_room, emit
# ct stores current time


app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://agnanimayur:0YfnfbZWmMQfC6Vc@cluster0.d7w8l8l.mongodb.net/user_db"
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to a strong secret key
app.config['REDIS_HOST'] = 'redis'
app.config['REDIS_PORT'] = 6379
app.config['REDIS_CACHE_KEY_PREFIX'] = 'chat_cache_'
mongo = PyMongo(app)
jwt = JWTManager(app)
client = MongoClient('mongodb+srv://agnanimayur:0YfnfbZWmMQfC6Vc@cluster0.d7w8l8l.mongodb.net/')
db = client['user_db']
users_collection = db['users']
chat_collection = db['chat']
redis_cache = redis.Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
socketio = SocketIO(app)


@app.route("/")
def home():
    return "Home Page"

