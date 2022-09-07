import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
from script import callmsg


aze = pytz.timezone('Asia/Baku')

schedule = BlockingScheduler()

trigger = OrTrigger([CronTrigger(day_of_week='mon-sun', hour='11', minute='05'),CronTrigger(day_of_week='mon-sun', hour='20', minute='46')])


schedule.add_job(callmsg, trigger, timezone=aze)
schedule.start()