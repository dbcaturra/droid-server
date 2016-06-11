#!/usr/bin/python

import datetime
import androidhelper

droid = androidhelper.Android()
now = datetime.datetime.now()
filename = "-".join(now.__str__().split(" "))
droid.recorderCaptureVideo("/storage/emulated/0/droid-server/flask_nodes/static/%s.jpg"%filename, duration=30,recordAudio=True)
