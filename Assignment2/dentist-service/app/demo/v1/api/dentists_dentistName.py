# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from ..database import database_controller

db_name = "z5266543.db"


class DentistsDentistname(Resource):

    def get(self, dentistName):

        query_result = database_controller(
            db_name, "SELECT * FROM Dentists WHERE dentist_name ='" + dentistName + "';")
        print(query_result, type(query_result))
        if not query_result:
            return {"result": "Sorry! We dont have any information for Dr. " + dentistName + ". Please choose from the list of dentists.",
                    "api_response": {
                        "code": 404,
                        "message": "Error! Not Found"}
                    }, 404, None
        return {"result": "Dr. " + query_result[0][0] + " is located at " + query_result[0][1] + " and specializes in " + query_result[0][2] + ".",
                "api_response": {
                "code": 200,
                "message": "Success!"}
                }, 200, None
