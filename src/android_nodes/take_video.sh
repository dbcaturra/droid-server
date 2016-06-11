#!/bin/sh
am start -a android.media.action.VIDEO_CAPTURE
sleep 5
input keyevent 27
sleep 30
input keyevent 27 &&
killall com.htc.camera
