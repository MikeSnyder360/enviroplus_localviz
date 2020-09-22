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
    filename=dir_path + "envirolog.txt",
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

data = {}
data["time"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)
data["temperature"] = bme280.get_temperature()
data["pressure"] = bme280.get_pressure()
data["humidity"] = bme280.get_humidity()

pms5003 = PMS5003()
try:
    readings = pms5003.read()
    print(readings)
except ReadTimeoutError:
    pms5003 = PMS5003()

data["pm"] = (readings.data)

ltr559 = LTR559()
data["lux"] = ltr559.get_lux()
data["prox"] = ltr559.get_proximity()

rrdtool.update(dir_path + "/rrd/temp.rrd", "N:%d" % (data["temperature"]))
rrdtool.update(dir_path + "/rrd/hum.rrd", "N:%d" % (data["humidity"]))
rrdtool.update(dir_path + "/rrd/lux.rrd", "N:%d" % (data["lux"]))
#rrdtool.update("rrd/pm.rrd", "N:%d:%d:%d:%d:%d:%d" % (*data[-8))

logging.info(json.dumps(data))
print(pprint.pprint(data))
time.sleep(1)




