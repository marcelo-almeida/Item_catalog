def get_category_list():
    return [
        {
            "name": "soccer",
            "id": 1
        },
        {
            "name": "basketball",
            "id": 2
        }
    ]


def get_lastest_items():
    return [
        {
            "cat_id": 1,
            "description": "test",
            "id": 1,
            "title": "jersey"
        },
        {
            "cat_id": 1,
            "description": "test2",
            "id": 2,
            "title": "jersey2"
        }
    ]


def get_item_list(category_name):
    return [
        {
            "cat_id": 1,
            "description": "test",
            "id": 3,
            "title": "jersey100"
        },
        {
            "cat_id": 1,
            "description": "test2",
            "id": 4,
            "title": "jersey200"
        }
    ]


def get_item(category_name, item_name):
    return {
        "cat_id": 1,
        "description": "test",
        "id": 3,
        "title": "jersey100"
    }
