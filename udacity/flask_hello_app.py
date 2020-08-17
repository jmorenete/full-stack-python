from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(_ _name__)
#in order to connect to our db we must set a config variable,
# which are set on the dictionary app.config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jmmore@localhost:5432/library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
    #typically, inside a class we'd specify an init method that would allow us
    # to initiliaze attributes whenever we create new object instances.
    # but sql alchemy does that for you
    # by default, sqlalchemy will make the lowercase name of class
    # the name of your table unless:
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    paying_member = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, name:{self.name}>'


db.create_all() # detects models and creates tables if dont exist


@app.route('/')
def index():
    firstPerson = Person.query.first()
    return 'Hello ' + firstPerson.name

if __name__ == '__main__':
    app.run()