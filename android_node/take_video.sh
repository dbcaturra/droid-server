#!/bin/bash
am start -a android.media.action.VIDEO_CAPTURE
input keyevent 27
sleep 30s
input keyevent 27
killall com.htc.camera
