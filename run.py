from flask import Flask, render_template
from service import get_category_list, get_lastest_items, \
    get_item_list, get_especific_item

app = Flask(__name__)


@app.route('/')
@app.route('/catalog')
def get_catalog():
    category_list = get_category_list()
    lastest_items = get_lastest_items()
    return render_template('catalog.html',
                           category_list=category_list,
                           lastest_items=lastest_items)


@app.route('/catalog/<int:category_id>/items')
def get_items(category_id):
    category_list = get_category_list()
    item_list = get_item_list(category_id)
    return render_template('items.html',
                           category_list=category_list,
                           item_list=item_list)


@app.route('/catalog/<int:category_id>/items/<int:item_id>')
def get_item(category_id, item_id):
    item = get_especific_item(category_id, item_id)
    return render_template('item.html',
                           item=item)


@app.route('/catalog/<int:category_id>/items/<int:item_id>/edit')
def edit_item(category_id, item_id):
    item = get_especific_item(category_id, item_id)
    return "edit item"


@app.route('/catalog/<int:category_id>/items/<int:item_id>/delete')
def edit_item(category_id, item_id):
    item = get_especific_item(category_id, item_id)
    return "delete item"


@app.route('/catalog/<int:category_id>/items/add')
def edit_item(category_id):
    return "add item"


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
