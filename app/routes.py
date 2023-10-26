from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faves')
def ski_images():
    images = [
        'ski1.jpg',
        'ski2.jpg',
        'ski3.jpg',
        'ski4.jpg',
        '/ki5.jpg',
    ]
    return render_template('skis.html', images=images)


