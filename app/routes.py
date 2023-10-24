from app import app
from flask import Flask, render_template



@app.route('/')
def index():
    name = 'Humans'
    skis= ['POWABUNGA', 'Jeffery 110', 'Mango100', 'shredditor', 'domain']
    return render_template('index.html')

@app.route('/faves')
def faves():
    return render_template('faves.html')




