from backend import db


class User(db.Model):
    # Primary key column for the user table
    id = db.Column(db.Integer, primary_key=True)
    # Unique username column with a maximum length of 20 characters
    username = db.Column(db.String(20), unique=True, nullable=False)
    # Password column for storing user passwords
    password = db.Column(db.String(60), nullable=False)
    # Role column for defining user roles (e.g., admin, user)
    role = db.Column(db.String(20), nullable=False, default='user')

    def __repr__(self):
        return f"User('{self.username}')"
