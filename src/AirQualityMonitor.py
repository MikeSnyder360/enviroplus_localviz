import json
import os
import time
import redis

redis_client = redis.StrictRedis(host=os.environ.get('REDIS_HOST'), port=6379, db=0)

# from bme280 import BME280
from pms5003 import PMS5003, ReadTimeoutError
# from ltr559 import LTR559

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

"""
PM1.0 ug/m3 (ultrafine particles):                             4
PM2.5 ug/m3 (combustion particles, organic compounds, metals): 5
PM10 ug/m3  (dust, pollen, mould spores):                      5
PM1.0 ug/m3 (atmos env):                                       4
PM2.5 ug/m3 (atmos env):                                       5
PM10 ug/m3 (atmos env):                                        5
>0.3um in 0.1L air:                                            0
>0.5um in 0.1L air:                                            0
>1.0um in 0.1L air:                                            0
>2.5um in 0.1L air:                                            0
>5.0um in 0.1L air:                                            0
>10um in 0.1L air:                                             0

>>> p.read().data
(5, 7, 7, 5, 7, 7, 0, 0, 0, 0, 0, 0, 38664, 368)
"""

class AirQualityMonitor():

    def __init__(self):
        self.pms5003 = PMS5003()

    def get_measurement(self):
        try:
            readings = self.pms5003.read()
        except ReadTimeoutError:
            self.pms5003 = PMS5003()

        return {
            'time': int(time.time()),
            'measurement': readings.data,
        }

    def save_measurement_to_redis(self):
        """Saves measurement to redis db"""
        redis_client.lpush('measurements', json.dumps(self.get_measurement(), default=str))

    def get_last_n_measurements(self):
        """Returns the last n measurements in the list"""
        return [json.loads(x) for x in redis_client.lrange('measurements', 0, -1)]
