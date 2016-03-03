#!/usr/bin/env python
# -*- coding: utf-8 -*-

from connection import *

def help_bot(username):
    filename = "images/help.png"
    answer = "@"+username+" Here is some help to use WatchingNantes"
    try:
        api.update_with_media(filename, answer)
    except tweepy.TweepError as e:
        print "FAILED : help_bot function "
