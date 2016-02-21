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

    if status_code == 200:
        api.update_with_media(filename, "Surveillance camera "+ idCam +" - "+ name +" - "+now.strftime("%A %d %B %Y at %H:%M")+ " #Nantes")
