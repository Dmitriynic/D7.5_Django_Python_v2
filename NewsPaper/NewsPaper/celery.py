import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')
 
app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_mails_every_monday_8am': {
        'task':'news.tasks.send_new_mails_weekly',
        'schedule': crontab(hour=21, minute=54, day_of_week='saturday'),
    },
}
app.conf.timezone = 'Europe/Moscow'