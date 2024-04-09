from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin # type: ignore

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    image = db.Column(db.String(80))
    price = db.Column(db.Numeric(precision=10, scale=2))  # Using Numeric for decimal data type
