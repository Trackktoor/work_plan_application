from flask import Blueprint, render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')