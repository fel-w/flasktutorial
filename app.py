from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy.orm import defaultload, exc

app = Flask(__name__)

# Db location using relative path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Initializa database with settings from app
db = SQLAlchemy(app)

# Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Function to return info upon update in db
    def __repr__(self):
        return '<Task %r>' %self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding the task'
    else:
        # Get all the contents in the database and store them in tasks
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
