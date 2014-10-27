# -*- coding: utf-8 -*-

from flask import Flask

from extension import db
from web import web

SECRET_KEY = 'TeamBuilding'
DEBUG=True

SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/TBuilding'

app = Flask(__name__)
app.config.from_object(__name__)

db.init_app(app)

app.register_blueprint(web, url_prefix='/web')

with app.app_context():
    db.create_all()
    #print "ok"

if __name__ == '__main__':
    app.run()

