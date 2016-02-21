#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def download_image(filename, url):
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for data in request:
                image.write(data)
        return 200
    else:
        return 404
