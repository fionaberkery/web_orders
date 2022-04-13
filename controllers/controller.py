from flask import render_template # ADDED
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders=orders)