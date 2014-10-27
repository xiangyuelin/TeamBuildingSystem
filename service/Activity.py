# -*- coding: utf-8 -*-

from datetime import datetime

from extension import db
from models.model import Activity


def get_activity(id):
    acti = Activity.query.get(id)
    return acti


def add_activity(title, type, show, remark, validate_period, created_at, updated_at):
    acti = Activity(title=title, type=type, show=show, remark=remark, validate_period=validate_period, \
            created_at=created_at, updated_at=updated_at)
    db.session.add(acti)
    db.session.commit()


def delete_activity(id):
    acti = Activity.query.get(id)
    db.session.delete(acti)
    db.session.commit()


def invalidate_activity(id):
    acti = Activity.query.get(id)
    acti.show = False
    acti.updated_at = date.utcnow
    db.session.commit()


def update_activity(id, validate_period):
    acti = Activity.query.get(id)
    acti.validate_period = validate_period
    acti.updated_at = date.utcnow
    db.session.commit()





