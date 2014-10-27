# -*- coding: utf-8 -*-

from datetime import datetime

from extension import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), default="user")
    name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(20))
    email = db.Column(db.String(30))
    phone = db.Column(db.String(20))


class FruitVoting(db.Model):
    __tablename__ = "fruit_voting"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer)
    menber = db.Column(db.String)
    created_at = db.Column(db.Integer, default=datetime.utcnow)
    is_validated = db.Column(db.Boolean, default=True)


class ActivityVoting(db.Model):
    __tablename__ = "activity_voting"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    is_validated = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


class ActivityVotingOption(db.Model):
    __tablename__ = "activity_voting_option"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    activity_option_id = db.Column(db.Integer)


class FruitVotingOption(db.Model):
    __tablename__ = "fruit_voting_option"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    fruit_voting_id = db.Column(db.Integer)


class ActivityVotingResult(db.Model):
    __tablename__ = "activity_voting_result"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    activity_voting_option_id = db.Column(db.Integer)


class FruitVotingResult(db.Model):
    __tablename__ = "activity_voting_result"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    fruit_voting_option_id = db.Column(db.Integer)


#comment for the activities not for items
class Comment(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    activity_id = db.Column(db.Integer)
    content = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)






