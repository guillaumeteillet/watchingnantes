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
        try:
            api.update_with_media(filename, "Surveillance camera "+ idCam +" - "+ name +" - "+now.strftime("%A %d %B %Y at %H:%M")+ " #Nantes")
        except tweepy.TweepError as e:
            print "FAILED : specific_security_cam : "+ str(e.message[0]['code'])

def specific_security_cam(cursor, username, idCam):
    cursor.execute('SELECT * FROM cameras WHERE camera_id="'+idCam+'"')
    cam = cursor.fetchone()

    if str(cam) == "None":
        answer = "@"+username+" Sorry, This security camera is not available or does not exist."
        try:
            api.update_status(answer)
        except tweepy.TweepError as e:
            print "FAILED : specific_security_cam cam variable=none : "+ str(e.message[0]['code'])
        print "ANSWER : "+answer
    else:
        now = datetime.datetime.now()
        filename = "images/user.jpg"
        status_code = download_image(filename, cam[3])
        idCam = unicode(cam[1])
        name = unicode(cam[2])
        answer = "@"+username+" You asked the security camera "+ idCam +" - "+ name +" - "+now.strftime("%A %d %B %Y at %H:%M")+ " #Nantes"

        if status_code == 200:
            try:
                api.update_with_media(filename, answer)
            except tweepy.TweepError as e:
                try:
                    answer = "@"+username+" "+ idCam +" - "+ name +" - "+now.strftime("%A %d %B %Y at %H:%M")
                    api.update_with_media(filename, answer)
                except tweepy.TweepError as e:
                    print "FAILED : specific_security_cam : "+ str(e.message[0]['code'])
            print "ANSWER : " + answer
