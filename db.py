from app_1 import app, db
from app_1.models import User

with app.app_context():
    user = User.query.first()
    print(user)
    print(user.password)
