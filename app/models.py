from . import db


class Message(db.Model):

    __tablename__ = 'message'

    created = db.Column(db.TIMESTAMP, nullable=False)
    id = db.Column(db.String, primary_key=True, nullable=False)
    int_id = db.Column(db.String(16), nullable=False)
    str = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean)

    __table_args__ = (
        db.Index('message_created_idx', 'created'),
        db.Index('message_int_id_idx', 'int_id'),
    )


class Log(db.Model):

    __tablename__ = 'log'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.TIMESTAMP, nullable=False)
    int_id = db.Column(db.String(16), nullable=False)
    str = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)

    __table_args__ = (
        db.Index('log_address_idx', 'address', postgresql_using='hash'),
    )
