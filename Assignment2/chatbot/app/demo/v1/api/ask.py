# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import os
from flask import request, g
from . import Resource
from .. import schemas
from rivescript import RiveScript
import requests
from urllib.parse import quote

bot = RiveScript()
bot.load_directory(os.path.join(os.path.dirname(__file__), ".", "brain"))
bot.sort_replies()


class Ask(Resource):

    def get(self):
        print(g.args.get("query"))
        msg = g.args.get("query")
        reply = bot.reply("mohitkhanna", msg)
        print(reply)
        if "ERR" in reply:
            reply = "I dont know this :( ask me something else"
        elif "listDentists=" in reply:
            url = "http://0.0.0.0:8888/v1/dentists"
            try:
                res = requests.get(url)
                res = res.json()
                print(res, res['result'], type(res['result']))
                reply = reply.replace("listDentists=", res['result'])
            except requests.exceptions.RequestException as e:
                reply = "System under maintenance. Please try again later!"
        elif "dentistInfo=" in reply:
            dentist = reply.split("=")[1].split("\n")[0]
            url = "http://0.0.0.0:8888/v1/dentists/" + dentist.capitalize()
            print(reply)
            try:
                res = requests.get(url)
                res = res.json()
                print(res)
                reply = reply.replace("dentistInfo=" + dentist, res['result'])
            except requests.exceptions.RequestException as e:
                reply = "System under maintenance. Please try again later!"
        elif "timeslots=" in reply:
            dentist = reply.split("=")[1].split("\n")[0]
            url = "http://0.0.0.0:4444/v1/timeslots/" + dentist.capitalize()
            print(reply)
            try:
                res = requests.get(url)
                res = res.json()
                print(res)
                reply = reply.replace("timeslots=" + dentist, res['result'])
            except requests.exceptions.RequestException as e:
                reply = "System under maintenance. Please try again later!"
        elif "bookAppointment=" in reply:
            temp = reply.split("=")[1].split("\n")[0]
            dentist = temp.split("@")[0]
            timeslot = temp.split("@")[1]
            url = "http://0.0.0.0:4444/v1/timeslots/{}/dentist/{}/book".format(
                quote(timeslot.capitalize()), quote(dentist.capitalize()))
            print(reply)
            print(url)
            try:
                res = requests.put(url)
                res = res.json()
                print(res)
                reply = reply.replace(
                    "bookAppointment=" + dentist + "@" + timeslot, res['result'])
            except requests.exceptions.RequestException as e:
                reply = "System under maintenance. Please try again later!"
        elif "yes=" in reply:
            temp = reply.replace("yes=", "")
            reply_array = temp.split(",")
            print(reply_array)
            if reply_array[0] and reply_array[1] and not reply_array[2] and not reply_array[3]:
                dentist = reply_array[0]
                timeslot = reply_array[1]
                url = "http://0.0.0.0:4444/v1/timeslots/{}/dentist/{}/book".format(
                    quote(timeslot.capitalize()), quote(dentist.capitalize()))
                print(reply)
                print(url)
                try:
                    res = requests.put(url)
                    res = res.json()
                    print(res)
                    reply = res['result']
                except requests.exceptions.RequestException as e:
                    reply = "System under maintenance. Please try again later!"

            elif reply_array[2] and reply_array[3] and not reply_array[0] and not reply_array[1]:
                dentist = reply_array[2]
                timeslot = reply_array[3]
                url = "http://0.0.0.0:4444/v1/timeslots/{}/dentist/{}/cancel".format(
                    quote(timeslot.capitalize()), quote(dentist.capitalize()))
                print(reply)
                print(url)
                try:
                    res = requests.put(url)
                    res = res.json()
                    print(res)
                    reply = res['result']
                except requests.exceptions.RequestException as e:
                    reply = "System under maintenance. Please try again later!"
            else:
                reply = "I dont know this :( ask me something else"

        return {"response": reply, "query": msg, "api_response": {"code": 200, "message": "Success!"}}, 200, None


def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


def create_app():
    app = Flask(__name__, static_folder='static')
    app.after_request(after_request)
    app.register_blueprint(
        v1.bp,
        url_prefix='/v1')
    return app
