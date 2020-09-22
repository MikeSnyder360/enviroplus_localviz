# enviroplus

Follow setup instructions from https://github.com/pimoroni/enviroplus-python to get PM sensor working with rpi

Run create_rrd.py to create rrd folder and rrd files

Use cron to execute

* * * * * /usr/bin/python /home/pi/enviroplus/enviroplus.py

This assumes a configuration or a enviro+ with PM5003. 


