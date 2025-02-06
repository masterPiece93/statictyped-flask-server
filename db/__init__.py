import sqlite3
from flask import g
from constants import DATABASE


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def inititalize(app):

    with app.app_context():
        db = get_db()
        with app.open_resource('db/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def insert_seed_data(app):

    with app.app_context():
        db = get_db()
        cur = db.cursor()

        class Query:
            InsertUser: str = "INSERT INTO user (username, firstname, lastname, email) VALUES (?, ?, ?, ?)"
            InsertNote: str = "INSERT INTO notes (title, content, created_by) VALUES (?, ?, ?)"
        try:
            seed_user1 = Query.InsertUser,\
                    ('system', 'system', 'system', 'system@ankit.in')
            seed_post1 = Query.InsertNote,\
                    ('Sample Note', 'This Note will guide you , how to use this app', 1)
            
            cur.execute(*seed_user1)
            cur.execute(*seed_post1)
        except Exception as e:
            raise e
        else:
            db.commit()
        finally:
            cur.close()
            db.close()
