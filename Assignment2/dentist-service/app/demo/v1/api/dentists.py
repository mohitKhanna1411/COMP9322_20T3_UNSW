# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from ..database import database_controller

db_name = "z5266543.db"


class Dentists(Resource):

    def get(self):
        query_result = database_controller(
            db_name, "SELECT dentist_name FROM Dentists;")
        print(query_result[0], type(query_result[0]))
        return {"result": "Available dentists are " + ','.join(str(y) for x in query_result for y in x if len(x) > 0),
                "api_response": {
                "code": 200,
                "message": "Success!"}
                }, 200, None
