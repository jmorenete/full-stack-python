import sys

from flask import (Flask, abort, jsonify, redirect, render_template, request,
                   url_for)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jmmore@localhost:5432/todoapp'
db = SQLAlchemy(app)

migrate  = Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=True,
    default=False)
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'


# db.create_all()


@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.get_json()['description']#request.form.get('description', '')
    error = False
    body = {}
    try:
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        db.session.rollback()
        error=True
        print(sys.exc_info())
    finally:
        db.session.close()
    
    if not error:
        return jsonify({
            'description': todo.description
        })
    else:
        abort(400)
    #return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())


if __name__ == '__main__':
    app.run(debug=True)
