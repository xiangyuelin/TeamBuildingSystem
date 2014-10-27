# -*- coding: utf-8 -*-

from flask import Blueprint

from service import User
from service import Activity
from service import Comment
from service import Item
from service import Vote

web = Blueprint('web', __name__)

@web.route('/')
def test():
    return "ok"
