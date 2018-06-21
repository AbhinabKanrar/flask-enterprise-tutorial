from app import db


def save(data):
    db.session.add(data)
    db.session.commit()
    return data