from flask import Flask, render_template


products = [
    {'id': 1, 'name': 'Футболка с капибарой', 'price': 999, 'image': '/static/images/capybara.jpg', 'description': 'Футболка с капибарой'},
    {'id': 2, 'name': 'Футболка с дачей', 'price': 1269, 'image': 'static/images/dacha_troops.jpg', 'description': 'Футболка с дачей'},
    {'id': 3, 'name': 'Футболка с Гомером', 'price': 1999, 'image': 'static/images/homer_simpson.jpg', 'description': 'Футболка с Гомером'},
    {'id': 4, 'name': 'Футболка Ольга босс', 'price': 1699, 'image': 'static/images/olga_boss.jpg', 'description': 'Футболка Ольга босс'},
    {'id': 5, 'name': 'Футболка Марк Скаут', 'price': 1199, 'image': 'static/images/mark_scout.jpg', 'description': 'Футболка Марк Скаут'},
    {'id': 6, 'name': 'Футболка кот', 'price': 1549, 'image': 'static/images/cat.jpg', 'description': 'Футболка кот'},
    {'id': 7, 'name': 'Футболка Друзья', 'price': 899, 'image': 'static/images/friends.jpg', 'description': 'Футболка Друзья'},
    {'id': 8, 'name': 'Футболка Гагарин', 'price': 2539, 'image': 'static/images/gagarin.jpg', 'description': 'Футболка Гагарин'},
    {'id': 9, 'name': 'Футболка Ведьмак', 'price': 3299, 'image': 'static/images/witcher.jpg', 'description': 'Футболка Ведьмак'}
]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
