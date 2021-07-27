# enviroplus

Follow setup instructions from https://github.com/pimoroni/enviroplus-python to get PM sensor working with rpi

Clone this repository into /home/pi (or wherever, make sure cron knows)

Run create_rrd.py to create rrd folder and rrd files

```
$ python create_rrd.py
```

Use cron to execute

```
crontab -e 
* * * * * /usr/bin/python /home/pi/enviroplus_localviz/src/enviroplus.py
* * * * * /usr/bin/python /home/pi/enviroplus_localviz/src/noise.py
```

This assumes a configuration or a enviro+ with PM5003. 


# installing DRRAW to view RRD data

install apache2
unzip drraw into /usr/lib/cgi-bin (https://web.taranis.org/drraw/)
restart apache
see if http://ip.address/cgi-bin/drraw/drraw.cgi loads

copy graphs and dashboards from drraw folder to /var/lib/drraw

