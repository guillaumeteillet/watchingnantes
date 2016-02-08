#!/usr/bin/env python

import sqlite3

def connect_db():
    return sqlite3.connect('database.db')

