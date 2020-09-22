import rrdtool
import os

if not os.path.exists('rrd'):
    os.makedirs('rrd')

filename = 'rrd/temp.rrd'
if not os.path.exists(filename):
    rrdtool.create(filename,
                 '--start', "now",
                 '--step', "1",
                 'DS:temp:GAUGE:300:0:50',
                 'RRA:AVERAGE:0.5:60:129600', 
                 'RRA:AVERAGE:0.5:3600:13392', 
                 'RRA:AVERAGE:0.5:86400:3660')

filename = 'rrd/hum.rrd'
if not os.path.exists(filename):
    rrdtool.create(filename,
                 '--start', "now",
                 '--step', "1",
                 'DS:hum:GAUGE:300:0:100',
                 'RRA:AVERAGE:0.5:60:129600', 
                 'RRA:AVERAGE:0.5:3600:13392', 
                 'RRA:AVERAGE:0.5:86400:3660')

filename = 'rrd/lux.rrd'
if not os.path.exists(filename):
    rrdtool.create(filename,
                 '--start', "now",
                 '--step', "1",
                 'DS:lux:GAUGE:300:0:50000',
                 'RRA:AVERAGE:0.5:60:129600', 
                 'RRA:AVERAGE:0.5:3600:13392', 
                 'RRA:AVERAGE:0.5:86400:3660')

filename = 'rrd/pm.rrd'
if not os.path.exists(filename):
    rrdtool.create(filename,
                 '--start', "now",
                 '--step', "1",
                 'DS:pm1_0_0:GAUGE:300:0:1000',
                 'DS:pm2_5_0:GAUGE:300:0:1000',
                 'DS:pm10_0:GAUGE:300:0:1000',
                 'DS:pm1_0_1:GAUGE:300:0:1000',
                 'DS:pm2_5_1:GAUGE:300:0:1000',
                 'DS:pm10_1:GAUGE:300:0:1000',
                 'RRA:AVERAGE:0.5:60:129600', 
                 'RRA:AVERAGE:0.5:3600:13392', 
                 'RRA:AVERAGE:0.5:86400:3660')

filename = 'rrd/noise.rrd'
if not os.path.exists(filename):
    rrdtool.create(filename,
                 '--start', "now",
                 '--step', "1",
                 'DS:noise0:GAUGE:300:0:100',
                 'DS:noise1:GAUGE:300:0:100',
                 'DS:noise2:GAUGE:300:0:100',
                 'DS:noise3:GAUGE:300:0:100',
                 'RRA:AVERAGE:0.5:1:129600', 
                 'RRA:AVERAGE:0.5:60:129600', 
                 'RRA:AVERAGE:0.5:3600:13392', 
                 'RRA:AVERAGE:0.5:86400:3660')

