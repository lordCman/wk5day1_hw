from hw import hw 
from flask import render_template

@hw.route('/')
def home1():
    return render_template('home1.html')

@hw.route('/fivefavoritethings')
def fiveFavThings():
    return render_template('fiveFavThings.html')