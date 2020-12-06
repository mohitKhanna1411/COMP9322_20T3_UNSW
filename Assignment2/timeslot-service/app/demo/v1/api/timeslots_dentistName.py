# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..database import database_controller

from . import Resource
from .. import schemas

db_name = "z5266543.db"


class TimeslotsDentistname(Resource):

    def get(self, dentistName):

        query_result = database_controller(
            db_name, "SELECT dentist_name FROM Appointments WHERE dentist_name='" + dentistName + "';")
        print(query_result)

        if not query_result:
            return {"result": "We dont have any information for Dr. " + dentistName + ". Please choose from the list of dentists.",
                    "api_response": {
                        "code": 404,
                        "message": "Error! Not Found"}
                    }, 404, None
        query_result = database_controller(
            db_name, "SELECT timeslot FROM Appointments WHERE dentist_name='" + dentistName + "' and status=0;")
        print(query_result)

        if not query_result:
            return {"result": "Sorry! Dr. " + dentistName + " is not available. Please book another dentist from the list.",
                    "api_response": {
                "code": 200,
                "message": "Success!"}
            }, 200, None

        return {"result": "Avaiablity of Dr. " + dentistName + ": " + ','.join(str(y) for x in query_result for y in x if len(x) > 0),
                "api_response": {
                "code": 200,
                "message": "Success!"}
                }, 200, None
