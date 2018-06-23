from flask import Flask, render_template, request, redirect, url_for, \
    jsonify, flash
from flask import session as login_session
from database_config import Item
from service import get_category_list, get_category_by_id, \
    get_item_list, get_item_by_id, count_items_by_category, \
    add_new_item, edit_item_by_id, delete_item_by_id, validate_item
from authorization_service import get_state, validate_user, \
    try_disconnect, CLIENT_ID
import requests

app = Flask(__name__)


@app.route('/')
@app.route('/catalog')
def get_catalog():
    category_list = get_category_list()
    lastest_items = get_item_list(None, 9)
    if 'username' not in login_session:
        template = render_template('publiccatalog.html',
                                   category_list=category_list,
                                   lastest_items=lastest_items,
                                   login="disconnected")
    else:
        template = render_template('catalog.html',
                                   category_list=category_list,
                                   lastest_items=lastest_items,
                                   login="connected")
    return template


@app.route('/catalog/JSON')
def get_catalog_json():
    categories = get_category_list()
    return jsonify(Category=[c.serialize_with_item for c in categories])


@app.route('/catalog/<int:category_id>/items')
def get_items(category_id):
    category_list = get_category_list()
    category = get_category_by_id(category_id)
    item_list = get_item_list(category_id, None)
    count = count_items_by_category(category_id)
    if 'username' in login_session:
        login = 'connected'
    else:
        login = 'disconnected'
    return render_template('items.html',
                           category_list=category_list,
                           category=category,
                           item_list=item_list,
                           count=count,
                           login=login)


@app.route('/catalog/<int:category_id>/items/JSON')
def get_items_json(category_id):
    category = get_category_by_id(category_id)
    return jsonify(Category=[category.serialize_with_item])


@app.route('/catalog/<int:category_id>/items/<int:item_id>')
def get_item(category_id, item_id):
    item = get_item_by_id(item_id)
    if 'username' not in login_session:
        template = render_template('publicitem.html',
                                   item=item,
                                   login="disconnected")
    else:
        template = render_template('item.html',
                                   item=item,
                                   login="connected")
    return template


@app.route('/catalog/<int:category_id>/items/<int:item_id>/JSON')
def get_item_json(category_id, item_id):
    item = get_item_by_id(item_id)
    return jsonify(Item=[item.serialize_with_category])


@app.route('/catalog/<int:category_id>/items/<int:item_id>/edit',
           methods=['GET', 'POST'])
def edit_item(category_id, item_id):
    if 'username' not in login_session:
        return redirect('/login')
    item = get_item_by_id(item_id)
    if request.method == 'POST':
        item.title = request.form['title']
        item.description = request.form['description']
        item.category_id = request.form['category']
        errors = validate_item(item)
        if not errors:
            edit_item_by_id(item)
            flash('Item %s Successfully Updated' % item.title)
            return redirect(url_for('get_item', category_id=category_id,
                                    item_id=item.id))
        else:
            for error in errors:
                flash(error)
            return redirect(url_for('edit_item',
                                    category_id=category_id,
                                    item_id=item.id))
    else:
        category_list = get_category_list()
    return render_template('form.html', category_list=category_list,
                           item=item,
                           action_title="Edit Item",
                           login="connected")


@app.route('/catalog/<int:category_id>/items/<int:item_id>/delete',
           methods=['GET', 'POST'])
def delete_item(category_id, item_id):
    if 'username' not in login_session:
        return redirect('/login')
    item = get_item_by_id(item_id)
    if request.method == 'POST':
        delete_item_by_id(item)
        flash('Item %s Successfully Deleted' % item.title)
        return redirect(url_for('get_items', category_id=category_id))
    else:
        return render_template('deleteitem.html', item=item, login="connected")


@app.route('/catalog/items/add', methods=['GET', 'POST'])
def add_item():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        item = Item(title=request.form['title'],
                    description=request.form['description'],
                    category_id=request.form['category'])
        errors = validate_item(item)
        if not errors:
            add_new_item(item)
            flash('New Item %s Successfully Created' % item.title)
            return redirect(url_for('get_catalog'))
        else:
            for error in errors:
                flash(error)
            return redirect(url_for('add_item'))
    else:
        category_list = get_category_list()
        return render_template('form.html', category_list=category_list,
                               item={},
                               action_title="Add Item",
                               login="connected")


@app.route('/login')
def show_login():
    state = get_state()
    if 'username' not in login_session:
        response = render_template('login.html',
                                   STATE=state,
                                   login="disconnected",
                                   client_id=CLIENT_ID)
    else:
        print('fail')
        response = redirect(url_for('get_catalog'))
    return response


@app.route('/connect', methods=['POST'])
def connect():
    response = validate_user(request, requests)
    return response


@app.route('/disconnect')
def disconnect():
    response = try_disconnect()
    if '200' not in str(response):
        return response
    else:
        # Reset the user's session.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        return redirect(url_for('get_catalog'))


if __name__ == '__main__':
    app.secret_key = 'my_super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
