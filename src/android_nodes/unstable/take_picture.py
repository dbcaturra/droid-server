#!/usr/bin/python

import datetime
import androidhelper

droid = androidhelper.Android()
now = datetime.datetime.now()
filename = "-".join(now.__str__().split(" "))
droid.cameraCapturePicture("/storage/emulated/0/droid-server/src/flask_nodes/static/%s.jpg"%filename, useAutoFocus=True)
