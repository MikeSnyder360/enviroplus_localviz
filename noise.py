import os
import time
import rrdtool

from enviroplus.noise import Noise
noise = Noise()

dir_path = os.path.dirname(os.path.realpath(__file__))

starttime = time.time()

# run roughly 1 Hz every minute scheduled by cron
while time.time() - starttime < 60:
    amp = noise.get_noise_profile()
    print(amp)
    rrdtool.update(dir_path + "/rrd/noise.rrd", "N:{}:{}:{}:{}".format(*amp))
    time.sleep(1)

