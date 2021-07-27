import os
import time
import rrdtool

from enviroplus.noise import Noise
noise = Noise()

dir_path = os.path.dirname(os.path.realpath(__file__))

starttime = time.time()

# TODO XXX this data doesn't look great as 4 line plots overlapping, make better
# possibly use the other amplitude @ frequency API and use several RRDs

# rrdtool can only support 1 Hz data, so if this isn't the right tool for this particular job...

# run roughly 1 Hz every ~minute scheduled by cron
while time.time() - starttime < 55:
    amp = noise.get_noise_profile()
    print(amp)
    rrdtool.update(dir_path + "/rrd/noise.rrd", "N:{}:{}:{}:{}".format(*amp))
    time.sleep(1)

