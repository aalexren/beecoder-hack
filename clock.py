from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

from random import seed
from random import randint
from datetime import datetime

@sched.scheduled_job('interval', seconds=5)
def timed_job():
    f = open("app/static/qr_file/qr_file.txt", "w")
    seed(datetime.now())
    qr_num = randint(1, 100000000)
    f.write(str(qr_num))
    f.close()

sched.start()