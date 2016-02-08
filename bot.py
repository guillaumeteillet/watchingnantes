#!/usr/bin/env python
 
from connection import *

argfile = str(sys.argv[1])

api.update_status(argfile)
