#!/usr/bin/env python
 
from connection import *
from download import *

txt = str(sys.argv[1])
filename = "images/cam.jpg"

status_code = download_image(filename, "http://infotrafic.nantesmetropole.fr/data/webcams/rt742.jpg")
if status_code == 200:
    api.update_with_media(filename, txt)
