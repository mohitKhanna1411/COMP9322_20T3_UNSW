# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.timeslots_dentistName import TimeslotsDentistname
from .api.timeslots_timeslot_dentist_dentistName_cancel import TimeslotsTimeslotDentistDentistnameCancel
from .api.timeslots_timeslot_dentist_dentistName_book import TimeslotsTimeslotDentistDentistnameBook


routes = [
    dict(resource=TimeslotsDentistname, urls=['/timeslots/<dentistName>'], endpoint='timeslots_dentistName'),
    dict(resource=TimeslotsTimeslotDentistDentistnameCancel, urls=['/timeslots/<timeslot>/dentist/<dentistName>/cancel'], endpoint='timeslots_timeslot_dentist_dentistName_cancel'),
    dict(resource=TimeslotsTimeslotDentistDentistnameBook, urls=['/timeslots/<timeslot>/dentist/<dentistName>/book'], endpoint='timeslots_timeslot_dentist_dentistName_book'),
]