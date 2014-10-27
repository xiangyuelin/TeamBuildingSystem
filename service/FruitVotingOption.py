# -*- coding: utf-8 -*-

from extension import db
from models.model import FruitVo# -*- coding: utf-8 -*-

from extension import db
from models.model import FruitVotingOption


def get_fruit_voting_option(id):
    fruit_voting_option = FruitVotingOption.query.get(id)
    return fruit_voting_option


def delete_fruit_voting_option(id):
    fruit_voting_option = FruitVotingOption.query.get(id)
    db.session.delete(fruit_voting_option)
    db.session.commit()


def update_fruit_voting_option(id, content):
    fruit_voting_option = FruitVotingOption.query.get(id)
    fruit_voting_option.content = content
    db.session.commit()


def add_fruit_voting_option(user_id, activity_id, content):
    fruit_voting_option = FruitVotingOption(user_id=user_id, activity_id=activity_id, content=content)
    db.session.add(fruit_voting_option)
    db.session.commit()


def get_all_fruit_voting_options(activity_id):
    fruit_voting_option = FruitVotingOption.query.filter_by(activity_id=activity_id).all()
    return fruit_voting_option
tingOption


def get_fruit_voting_option(id):
    fruit_voting_option = FruitVotingOption.query.get(id)
    return fruit_voting_option


def delete_fruit_voting_option(id):
    fruit_voting_option = FruitVotingOption.query.get(id)
    db.session.delete(fruit_voting_option)
    db.session.commit()


def update_fruit_voting_option(id, content):
    fruit_voting_option = FruitVotingOption.query.get(id)
    fruit_voting_option.content = content
    db.session.commit()


def add_fruit_voting_option(user_id, activity_id, content):
    fruit_voting_option = FruitVotingOption(user_id=user_id, activity_id=activity_id, content=content)
    db.session.add(fruit_voting_option)
    db.session.commit()


def get_all_fruit_voting_options(activity_id):
    fruit_voting_option = FruitVotingOption.query.filter_by(activity_id=activity_id).all()
    return fruit_voting_option
