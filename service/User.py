# -*- coding: utf-8 -*-

from extension import db
from models.model import User


def get_user(id):
    user = User.query.get(id)
    return user


def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()


def add_user(name, pwd, email, phone):
    user = User(name=name, password=pwd, email=email, phone=phone)
    db.session.add(user)
    db.session.commit()


def update_user(id, pwd, email, phone):
    user = User.query.get(id)
    user.pwd = pwd
    user.email = email
    user.phone = phone
    db.session.commit()


