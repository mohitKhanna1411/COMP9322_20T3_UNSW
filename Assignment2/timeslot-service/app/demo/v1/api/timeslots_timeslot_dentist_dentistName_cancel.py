# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..database import database_controller

from . import Resource
from .. import schemas
db_name = "z5266543.db"


class TimeslotsTimeslotDentistDentistnameCancel(Resource):

    def put(self, timeslot, dentistName):
        query_result = database_controller(
            db_name, "SELECT * FROM Appointments WHERE dentist_name='" + dentistName + "' and timeslot = '" + timeslot + "';")
        print(query_result)
        if not query_result:
            return {"result": "We dont have any information for Dr. " + dentistName + " or " + timeslot + " timeslot. Please try again.",
                    "api_response": {
                        "code": 404,
                        "message": "Error! Not Found"}
                    }, 404, None
        query_result = database_controller(
            db_name, "UPDATE Appointments SET status = 0 WHERE dentist_name='" + dentistName + "' and timeslot = '" + timeslot + "';")
        print(query_result)
        return {"result": "Appointment with Dr. " + dentistName + " for " + timeslot + " has been cancelled.",
                "api_response": {
                    "code": 200,
                    "message": "Success!"}
                }, 200, None
