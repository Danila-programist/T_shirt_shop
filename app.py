from flask import Flask, render_template, request
import math

products = [
    {'id': 1, 'name': 'Футболка с капибарой', 'price': 999, 'image': '/static/images/capybara.jpg', 'description': 'Футболка с капибарой'},
    {'id': 2, 'name': 'Футболка с дачей', 'price': 1269, 'image': 'static/images/dacha_troops.jpg', 'description': 'Футболка с дачей'},
    {'id': 3, 'name': 'Футболка с Гомером', 'price': 1999, 'image': 'static/images/homer_simpson.jpg', 'description': 'Футболка с Гомером'},
    {'id': 4, 'name': 'Футболка Ольга босс', 'price': 1699, 'image': 'static/images/olga_boss.jpg', 'description': 'Футболка Ольга босс'},
    {'id': 5, 'name': 'Футболка Марк Скаут', 'price': 1199, 'image': 'static/images/mark_scout.jpg', 'description': 'Футболка Марк Скаут'},
    {'id': 6, 'name': 'Футболка кот', 'price': 1549, 'image': 'static/images/cat.jpg', 'description': 'Футболка кот'},
    {'id': 7, 'name': 'Футболка Друзья', 'price': 899, 'image': 'static/images/friends.jpg', 'description': 'Футболка Друзья'},
    {'id': 8, 'name': 'Футболка Гагарин', 'price': 2539, 'image': 'static/images/gagarin.jpg', 'description': 'Футболка Гагарин'},
    {'id': 9, 'name': 'Футболка Ведьмак', 'price': 3299, 'image': 'static/images/witcher.jpg', 'description': 'Футболка Ведьмак'},
    {'id': 10, 'name': 'Футболка Гаччи', 'price': 1269, 'image': 'static/images/gachi.jpg', 'description': 'Футболка Гаччи'},
    {'id': 11, 'name': 'Футболка Самурай', 'price': 759, 'image': 'static/images/samurai.jpg', 'description': 'Футболка Самурай'}
]

app = Flask(__name__)


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total = len(products)
    pages = math.ceil(total / per_page)

    start = (page - 1) * per_page
    end = start + per_page
    current_products = products[start:end]

    return render_template('index.html', products=current_products, page=page, pages=pages)

if __name__ == '__main__':
    app.run(debug=True)