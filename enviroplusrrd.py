#!/usr/bin/env python3

import datetime 
import os
import time
import json
import logging
import pprint

from bme280 import BME280
from pms5003 import PMS5003, ReadTimeoutError
from ltr559 import LTR559

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

import rrdtool

dir_path = os.path.dirname(os.path.realpath(__file__))

logging.basicConfig(
    filename="%s/envirolog.txt" % dir_path,
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

data = {}
data["time"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

bus = SMBus(1)
time.sleep(0.1)
bme280 = BME280(i2c_dev=bus)
time.sleep(0.5)
data["temperature"] = bme280.get_temperature()
time.sleep(0.5)
data["temperature"] = bme280.get_temperature()
time.sleep(0.1)
data["pressure"] = bme280.get_pressure()
time.sleep(0.1)
data["humidity"] = bme280.get_humidity()

pms5003 = PMS5003()
try:
    readings = pms5003.read()
    print(readings)
except ReadTimeoutError:
    pms5003 = PMS5003()

data["pm"] = readings.data

ltr559 = LTR559()
time.sleep(0.1)
data["lux"] = ltr559.get_lux()

logging.info(json.dumps(data))
print(pprint.pprint(data))

rrdtool.update(dir_path + "/rrd/temp.rrd", "N:%d" % (data["temperature"]))
rrdtool.update(dir_path + "/rrd/hum.rrd", "N:%d" % (data["humidity"]))
rrdtool.update(dir_path + "/rrd/pres.rrd", "N:%d" % (data["pressure"]))
rrdtool.update(dir_path + "/rrd/lux.rrd", "N:%d" % (data["lux"]))
rrdtool.update(dir_path + "/rrd/pm.rrd", ("N" + ":{}"*6).format(*data["pm"][:-8])) 





