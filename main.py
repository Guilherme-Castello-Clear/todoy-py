from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"

db = SQLAlchemy(app)


class Tasks(db.Model):
	__tablename__ = "tasks"
	id = Column(Integer, primary_key=True)
	title = Column(String, nullable=False)
	is_done = Column(db.Boolean, unique=False, default=False)


with app.app_context():
	db.create_all()


@app.route('/done', methods=['POST'])
def done():
	update_task = db.get_or_404(Tasks, request.form.get('id'))
	update_task.is_done = True
	db.session.commit()
	return redirect('/')


@app.route('/')
def home():
	tasks = Tasks.query.all()
	return render_template("index.html", tasks=tasks)


@app.route("/add", methods=['POST', 'GET'])
def new_task():
    add_task = Tasks(
        title=request.form.get('title')
    )
    db.session.add(add_task)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=5002)
