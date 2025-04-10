from flask import Flask, render_template


products = [
    {'id': 1, 'name': 'Футболка с капибарой', 'price': 999, 'image': '/static/images/capybara.jpg', 'description': 'Футболка с капибарой'},
    {'id': 2, 'name': 'Футболка с дачей', 'price': 1269, 'image': 'static/images/dacha_troops.jpg', 'description': 'Футболка с дачей'},
    {'id': 3, 'name': 'Футболка с Гомером', 'price': 1999, 'image': 'static/images/homer_simpson.jpg', 'description': 'Футболка с Гомером'},
    {'id': 3, 'name': 'Футболка Ольга босс', 'price': 1699, 'image': 'static/images/olga_boss.jpg', 'description': 'Футболка Ольга босс'}
]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
