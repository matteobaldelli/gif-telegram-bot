from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer)
    update_date = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    creation_date = db.Column(db.DateTime(timezone=True), server_default=db.func.now())

    def __init__(self, chat_id):
        self.chat_id = chat_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
