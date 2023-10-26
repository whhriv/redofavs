from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faves')
def ski_images():
    images = [
        'ski1.jpg',
        '/templates/ski2.jpg',
        './templates/ski3.jpg',
        '/ski4.jpg',
        '/ski5.jpg',
    ]
    return render_template('colors.html', images=images)

# @app.route('/skis')
# def img():
#     return render_template('skis.html')
