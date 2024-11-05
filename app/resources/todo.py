from flask_restful import Resource, reqparse
from ..models import TodoModel
from ..db import db

# Parser for the incoming request data
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help="Title cannot be blank!")
parser.add_argument('description', type=str)
parser.add_argument('done', type=bool)

class TodoListResource(Resource):
    def get(self):
        """Retrieve all todos"""
        todos = TodoModel.query.all()
        return [todo.to_dict() for todo in todos], 200

    def post(self):
        """Create a new todo"""
        args = parser.parse_args()

        if len(args['title']) == 0:
            return {"message": {"title": "Title cannot be blank!"}}, 404

        todo = TodoModel(
            title=args['title'],
            description=args.get('description', ''),
            done=args.get('done', False)
        )
        db.session.add(todo)
        db.session.commit()
        return todo.to_dict(), 201


class TodoResource(Resource):
    """Get single todo by ID"""
    def get(self, todo_id):
        todo = TodoModel.query.get(todo_id)
        if not todo:
            return {"message": "Todo not found"}, 404
        return todo.to_dict(), 200

    """Update todo by ID"""
    def put(self, todo_id):  
        todo = TodoModel.query.get(todo_id)
        if not todo:
            return {"message": "Todo not found"}, 404

        args = parser.parse_args()
        todo.title = args['title']
        todo.description = args.get('description', todo.description)
        todo.done = args.get('done', todo.done)

        db.session.commit()
        return todo.to_dict(), 200

    """Delete todo by ID"""
    def delete(self, todo_id):  
        todo = TodoModel.query.get(todo_id)
        if not todo:
            return {"message": "Todo not found"}, 404

        db.session.delete(todo)
        db.session.commit()
        return '', 204
