# -*- coding: utf-8 -*-

from datetime import datetime

from extension import db
from models.model import ActivityVoting


def get_activity_voting(id):
    acti = ActivityVoting.query.get(id)
    return acti


def add_activity_voting(title, type, remark, validate_period):
    acti = ActivityVoting(title=title, type=type, remark=remark, validate_period=validate_period, \
            created_at=created_at, updated_at=updated_at)
    db.session.add(acti)
    db.session.commit()


def delete_activity_voting(id):
    acti = ActivityVoting.query.get(id)
    db.session.delete(acti)
    db.session.commit()


def invalidate_activity_voting(id):
    acti = ActivityVoting.query.get(id)
    acti.is_validated = False
    acti.updated_at = date.utcnow
    db.session.commit()


def get_all_activity_votings():
    activities = ActivityVoting.query.all()
    return activities


def get_current_activity_votings():
    activities = ActivityVoting.query.filter_by(show=True).all()
    return activities






