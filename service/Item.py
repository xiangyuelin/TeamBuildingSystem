# -*- coding: utf-8 -*-

from extension import db
from models.model import Item


def get_item(id):
    item = Item.query.get(id)
    return item


def delete_item(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()


def update_item(id, content):
    item = Item.query.get(id)
    item.content = content
    db.session.commit()


def add_item(user_id, activity_id, content):
    item = Item(user_id=user_id, activity_id=activity_id, content=content)
    db.session.add(item)
    db.session.commit()
