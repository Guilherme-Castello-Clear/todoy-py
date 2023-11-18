from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5002)