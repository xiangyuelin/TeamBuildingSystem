# -*- coding: utf-8 -*-

from extension import db
from models.model import Admin


def get_admin(id):
    admin = Admin.query.get(id)
    return admin


def delete_admin(id):
    admin = Admin.query.get(id)
    db.session.delete(admin)
    db.session.commit()


def add_admin(name, pwd):
    admin = Admin(name=name, password=pwd)
    db.session.add(user)
    db.session.commit()


def update_admin(id, pwd):
    admin = Admin.query.get(id)
    admin.pwd = pwd
    db.session.commit()
