from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Person(UserMixin, db.Model):
    id = id = db.Column(db.Integer, primary_key=True,
                        nullable=False, autoincrement=True, index=True)
    email = db.Column(db.String(35), nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<Person {}>'.format(self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return Person.query.get(int(id))


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, index=True)
    title = db.Column(db.String(100))
    file = db.Column(db.LargeBinary)

    def __repr__(self):
        return f"File('{self.title}')"


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, index=True)
    url = db.Column(db.String(200))
    title = db.Column(db.String(100))

    def __repr__(self):
        return f"Video('{self.url}')"


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False,
                   autoincrement=True, index=True)
    title = db.Column(db.String(100))
    text = db.Column(db.String(200))

    def __repr__(self):
        return f"Text('{self.text}')"
