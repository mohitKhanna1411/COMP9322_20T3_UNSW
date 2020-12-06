# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask
from v1.database import database_controller, create_db

import v1


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v1.bp,
        url_prefix='/v1')
    return app


db_name = "z5266543.db"

if __name__ == '__main__':
    create_db(db_name)

    create_app().run(host='0.0.0.0', port=4444)
