#!/bin/sh
am start -a android.media.action.IMAGE_CAPTURE;
sleep 2;
input keyevent 27;
echo "Signal key sended";
sleep 2;
#kill $(pidof com.htc.camera)                                                                                                                                         
echo "ready to kill";
#pkill -f com.htc.camera;
input keyevent 3;
