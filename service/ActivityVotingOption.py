# -*- coding: utf-8 -*-

from extension import db
from models.model import ActivityVotingOption


def get_activity_voting_option(id):
    option = ActivityVotingOption.query.get(id)
    return option


def delete_activity_voting_option(id):
    option = ActivityVotingOption.query.get(id)
    db.session.delete(option)
    db.session.commit()


def update_fruit_voting_option(id, content):
    option = ActivityVotingOption.query.get(id)
    option.content = content
    db.session.commit()


def add_activity_voting_option(user_id, activity_id, content):
    option = ActivityVotingOption(user_id=user_id, activity_id=activity_id, content=content)
    db.session.add(option)
    db.session.commit()


def get_all_activity_voting_options(activity_id):
    option = ActivityVotingOption.query.filter_by(activity_id=activity_id).all()
    return option
