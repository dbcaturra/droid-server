#!/bin/bash
#Perform in boot behavior
clear				# clear terminal window
echo "The script starts now."
echo "Hi, $USER!"		# dollar sign is used to get content of variable
echo

#getup qpython flask server (python scripts)
#run sensors_node (android bash script)
#load alarms_node (android bash script)

export FLASK_APP=/storage/emulated/0/DroidServer/android-ros-api.py
sh /data/data/com.hipipal.qpyplus/files/bin/qpython-android5.sh -m flask run --host=0.0.0.0

