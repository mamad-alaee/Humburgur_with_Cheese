from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from models.User import User
from models.Role import Role

schadular = BackgroundScheduler()


def say_hello():
    print("Hello, World!")

def backup_database():
    db = {
        "users" : User.objects(),
        "roles" : Role.objects()
    }


def create_jobs():
    print("creating jobs")
    # schadular.add_job(say_hello, 'interval', seconds=5)
    # schadular.add_job(say_hello, 'cron',hour='5', minute='10', second='20')

    trigger = CronTrigger(day_of_week="mon",hour=12,minute=30,second=0)
    schadular.add_job(say_hello, trigger)

    schadular.start()

