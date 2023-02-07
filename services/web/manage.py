import sys
from flask.cli import FlaskGroup
from flask_flatpages import FlatPages

from project import app, db, User


cli = FlaskGroup(app)
flatpages = FlatPages(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="nbaugh1@nbaugh1.com"))
    db.session.commit()

@cli.command("build")
def build():
    pass

if __name__ == "__main__":
        cli()