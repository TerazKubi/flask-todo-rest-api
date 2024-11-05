from app import create_app
from app.db import db
from app.models import TodoModel


app = create_app()
with app.app_context():
    db.create_all()

    random_todos = [
    {"title": "Buy groceries", "description": "Buy essentials for the week", "done": False},
    {"title": "Write blog post", "description": "Outline and write the first draft", "done": True},
    {"title": "Read a book", "description": "Read 50 pages", "done": False},
    {"title": "Clean the house", "description": "Organize and clean each room", "done": True},
    {"title": "Finish project report", "description": "Summarize project milestones", "done": False},
    {"title": "Prepare presentation", "description": "Create slides and notes", "done": True},
    {"title": "Water the plants", "description": "Water all indoor and outdoor plants", "done": False},
    {"title": "Go for a walk", "description": "Walk for 30 minutes", "done": True},
    {"title": "Complete coding assignment", "description": "Complete tasks by deadline", "done": False},
    {"title": "Plan weekend trip", "description": "Research and make itinerary", "done": True}
]

    for element in random_todos:
        new_todo = TodoModel(title= element['title'], description = element['description'], done = element['done'])
        db.session.add(new_todo)

    db.session.commit()