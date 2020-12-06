# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..database import database_controller

from . import Resource
from .. import schemas
db_name = "z5266543.db"


class TimeslotsTimeslotDentistDentistnameBook(Resource):

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
        if query_result[0][2] == 1:
            query_result = database_controller(
                db_name, "SELECT timeslot FROM Appointments WHERE dentist_name='" + dentistName + "' and status=0;")
            print(query_result)
            return {"result": "Sorry! " + timeslot + " is already booked please choose a different timeslot. Avaiablity of Dr. " + dentistName + ": " + ','.join(str(y) for x in query_result for y in x if len(x) > 0),
                    "api_response": {
                "code": 200,
                "message": "Success!"}
            }, 200, None
        query_result = database_controller(
            db_name, "UPDATE Appointments SET status = 1 WHERE dentist_name='" + dentistName + "' and timeslot = '" + timeslot + "';")
        print(query_result)
        return {"result": "Appointment with Dr. " + dentistName + " for " + timeslot + " sucessfully booked. Thanks!",
                "api_response": {
                    "code": 200,
                    "message": "Success!"}
                }, 200, None
