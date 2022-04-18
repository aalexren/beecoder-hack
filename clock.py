from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

from random import seed
from random import randint
from datetime import datetime
from os.path import join, dirname, realpath

qr_path = join(dirname(realpath(__file__)), 'app/static/qr_file/')

@sched.scheduled_job('interval', seconds=5)
def timed_job():
    f = open(join(qr_path, 'qr_file.txt'), "r")
    seed(datetime.now())
    qr_num = f.read()
    f.close()
    f = open(join(qr_path, 'qr_file.txt'), "w")
    qr_num = (int(qr_num) + 17) % 100000000
    f.write(str(qr_num))
    f.close()

sched.start()