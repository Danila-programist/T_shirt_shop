from flask import Flask, render_template


app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Горы на закате', 'price': 1200, 'image': '/static/poster1.jpg', 'description': 'Атмосферный пейзаж гор при закате.'},
    {'id': 2, 'name': 'Минималистичный лес', 'price': 950, 'image': '/static/poster2.jpg', 'description': 'Простой и стильный лесной постер.'},
    {'id': 3, 'name': 'Город в дождь', 'price': 1350, 'image': '/static/poster3.jpg', 'description': 'Городская романтика в каплях дождя.'}
]

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
