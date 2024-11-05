from flask import Flask
from flask_restful import Api
from .db import db
from .resources.todo import TodoResource, TodoListResource
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    api = Api(app)
    
    # Create tables if not present
    with app.app_context():
        db.create_all()

    # Define routes
    api.add_resource(TodoListResource, '/api/todos/')
    api.add_resource(TodoResource, '/api/todos/<int:todo_id>')

    return app