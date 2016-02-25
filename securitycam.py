#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from download import *
from connection import *

def random_security_cam(cursor):
    cursor.execute('SELECT * FROM cameras ORDER BY RANDOM() LIMIT 1')
    cam = cursor.fetchone()

    now = datetime.datetime.now()
    filename = "images/cam.jpg"
    status_code = download_image(filename, cam[3])
    idCam = unicode(cam[1])
    name = unicode(cam[2])
    status = "Surveillance camera "+ idCam +" - "+ name +" - "+now.strftime("%A %d %B %Y at %H:%M")+ " #Nantes"

    if status_code == 200:
        api.update_with_media(filename, status)
        print status

def specific_security_cam(cursor, username, idCam):
    cursor.execute('SELECT * FROM cameras WHERE camera_id="'+idCam+'"')
    cam = cursor.fetchone()

    if str(cam) == "None":
        api.update_status("@"+username+" Sorry, This security camera is not available or does not exist.")
    else:
        now = datetime.datetime.now()
        filename = "images/user.jpg"
        status_code = download_image(filename, cam[3])
        idCam = unicode(cam[1])
        name = unicode(cam[2])
        status = "@"+username+" You asked the security camera "+ idCam +" - "+ name +" - "+now.strftime("%A %d %B %Y at %H:%M")+ " #Nantes"

        if status_code == 200:
            api.update_with_media(filename, status)
            print status
