from flask import Flask, render_template, request, redirect, url_for
from service import get_category_list, get_category_by_id, get_lastest_items, \
    get_item_list, get_especific_item, count_items, add_new_item, \
    edit_item_by_id, delete_item_by_id
from database_config import Item

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
    category = get_category_by_id(category_id)
    item_list = get_item_list(category_id)
    count = count_items(category_id)
    return render_template('items.html',
                           category_list=category_list,
                           category=category,
                           item_list=item_list,
                           count=count)


@app.route('/catalog/<int:category_id>/items/<int:item_id>')
def get_item(category_id, item_id):
    item = get_especific_item(item_id)
    return render_template('item.html',
                           item=item)


@app.route('/catalog/<int:category_id>/items/<int:item_id>/edit',
           methods=['GET', 'POST'])
def edit_item(category_id, item_id):
    item = get_especific_item(item_id)
    if request.method == 'POST':
        item.title = request.form['title']
        item.description = request.form['description']
        item.category_id = request.form['category']
        edit_item_by_id(item)
        return redirect(url_for('get_item', category_id=category_id,
                                item_id=item.id))
    else:
        category_list = get_category_list()
    return render_template('form.html', category_list=category_list,
                           item=item,
                           action_title="Edit Item")


@app.route('/catalog/<int:category_id>/items/<int:item_id>/delete',
           methods=['GET', 'POST'])
def delete_item(category_id, item_id):
    item = get_especific_item(item_id)
    if request.method == 'POST':
        delete_item_by_id(item)
        return redirect(url_for('get_items', category_id=category_id))
    else:
        return render_template('deleteitem.html', item=item)


@app.route('/catalog/items/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item = Item(title=request.form['title'],
                    description=request.form['description'],
                    category_id=request.form['category'])
        add_new_item(item)
        return redirect(url_for('get_catalog'))
    else:
        category_list = get_category_list()
        return render_template('form.html', category_list=category_list,
                               item={},
                               action_title="Add Item")


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
