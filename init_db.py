from taskmanager import db
from taskmanager.models import Category, Task

with app.app_context():
    db.create_all()
