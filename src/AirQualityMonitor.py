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

class AirQualityMonitor():

    def __init__(self):
        self.pms5003 = PMS5003()

    def get_measurement(self):
        try:
            readings = self.pms5003.read()
            print(readings)
        except ReadTimeoutError:
            self.pms5003 = PMS5003()

        return {
            'time': int(time.time()),
            'measurement': self.readings.data,
        }

    def save_measurement_to_redis(self):
        """Saves measurement to redis db"""
        redis_client.lpush('measurements', json.dumps(self.get_measurement(), default=str))

    def get_last_n_measurements(self):
        """Returns the last n measurements in the list"""
        return [json.loads(x) for x in redis_client.lrange('measurements', 0, -1)]
