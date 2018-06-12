from flask import Flask, render_template
from service import get_category_list,get_lastest_items,\
    get_item_list, get_item

app = Flask(__name__)


@app.route('/')
@app.route('/catalog') 
def get_catalog():
    category_list = get_category_list()
    lastest_items = get_lastest_items()
    return render_template('catalog.html',
                           category_list=category_list,
                           lastest_items=lastest_items)


@app.route('/catalog/<string:category_name>/items')
def get_items(category_name):
    category_list = get_category_list()
    item_list = get_item_list(category_name)
    return render_template('items.html',
                           category_list=category_list,
                           item_list=item_list)


@app.route('/catalog/<string:category_name>/<string:item_name>')
def get_item(category_name, item_name):
    item = get_item(category_name, item_name)
    return render_template('item.html',
                           item=item)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
