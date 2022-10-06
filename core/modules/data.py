from flask_sqlalchemy import SQLAlchemy
from core import app


db = SQLAlchemy(app)


class data_bcg(db.Model):

    __tablename__ = 'databcg'

    id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(64),index=True)
    sku = db.Column(db.String(64))

    def __repr__(self):
        return '<name:{}'.format(self.name)