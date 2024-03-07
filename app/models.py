from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

EXCLUDED_FIELDS = ['creation_date', 'modified_date']


class BaseModel():
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creation_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    modified_date = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now, nullable=False)
    
    def to_dict(self):
        return {column.name: getattr(self, column.name, None) for column in self.__table__.columns if column.name not in EXCLUDED_FIELDS}
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

class User(BaseModel, db.Model):
    __tablename__ = 'user'

    username = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash =generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @staticmethod
    def is_exist(username):
        return User.query.filter_by(username=username).first()
