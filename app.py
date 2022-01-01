from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy.orm import defaultload

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

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
