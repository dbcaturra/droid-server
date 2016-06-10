#!/bin/sh
am start -a android.media.action.IMAGE_CAPTURE
sleep 5
input keyevent 27
killall com.htc.camera
