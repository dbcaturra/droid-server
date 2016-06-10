#!/bin/sh
am start -a android.media.action.IMAGE_CAPTURE
input keyevent 27
killall com.htc.camera
