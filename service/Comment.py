# -*- coding: utf-8 -*-

from extension import db
from models.model import Comment


def get_comment(id):
    comment = Comment.query.get(id)
    return comment


def delete_comment(id):
    comment = Comment.query.get(id)
    db.session.delete(comment)
    db.session.commit()


def add_comment(user_id, activity_id, content):
    comment = Comment(user_id=user_id, activity_id=activity_id, content=content)
    db.session.add(comment)
    db.session.commit()


def get_all_item_comment(item_id):
    comments = Comment.query.filter_by(item_id=item_id).all()
    return comments

