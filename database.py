#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def connect_db():
    return sqlite3.connect('database.db')
