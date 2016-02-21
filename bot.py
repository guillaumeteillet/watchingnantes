#!/usr/bin/env python
# -*- coding: utf-8 -*-

from connection import *
from download import *
from database import *
from securitycam import *

#txt = str(sys.argv[1])


client = connect_db()
cursor = client.cursor()


while True:
    random_security_cam(cursor)
    time.sleep(900)
