#!/usr/bin/env python
# -*- coding: utf-8 -*-

from connection import *
from download import *
from database import *
from securitycam import *
from help_bot import *

import time

client = connect_db()
cursor = client.cursor()

timerLastTweet = 0
timeLastCheck = 0

cursor.execute('SELECT * FROM parameters WHERE param="idLastMention"')
cam = cursor.fetchone()
idLastMention = int(cam[2])

while True:

    # Every 15 minutes (=900 sec), a new pic of a security cam
    if timerLastTweet == 0 or timerLastTweet + 900 < time.time():
        try:
            random_security_cam(cursor)
            timerLastTweet = time.time()
            print "Security cam has been tweeted"
        except tweepy.TweepError:
            time.sleep(120)
            print "FAILED"
            continue

    # Every minutes we check mentions
    if timeLastCheck == 0 or timeLastCheck + 60 < time.time():
        if idLastMention == 0:
            mymentions = api.mentions_timeline()
        else:
            try:
                mymentions = api.mentions_timeline(since_id=idLastMention)
            except tweepy.error.RateLimitError as e:
                time.sleep(120)
                print "FAILED READING MENTIONS ERROR CODE : "+ str(e.message[0]['code'])
                continue
        mymentions.reverse()
        for tweet in mymentions:
            try:
                print "MENTION : " + str(unicode(tweet.text).encode("utf-8"))+" FROM  "+str(unicode(tweet.user.screen_name).encode("utf-8"))
                cmd = str(unicode(tweet.text).encode("utf-8")).split()


                # Ask for a specific security camera
                if cmd[1] == "CAM":
                    specific_security_cam(cursor, str(unicode(tweet.user.screen_name)), str(cmd[2]))

                # Ask for help
                if cmd[1] == "HELP":
                    help_bot(str(unicode(tweet.user.screen_name)));

                cursor.execute('UPDATE parameters SET value="'+str(tweet.id)+'" WHERE param="idLastMention"')
                client.commit()
                idLastMention = tweet.id
            except tweepy.TweepError as e:
                time.sleep(120)
                print "FAILED ANALYZE MENTIONS ERROR CODE : "+ str(e.message[0]['code'])
                continue
        timeLastCheck = time.time()
