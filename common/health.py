from django.conf import settings
from django.http import JsonResponse
from common.tasks import test_celery
import requests


def health_check(request):
    return JsonResponse({
        'emis_status': emis_connection(),
        'celery_status': celery_connection()
    })


def emis_connection():
    emis_status = 'Down'
    response = requests.get(settings.EMIS_API_HOST, timeout=5)
    if response.status_code == 200:
        emis_status = 'Up'
    return emis_status


def celery_connection():
    celery_status = 'Down'
    task = test_celery.apply_async(args=[1,1])
    task.get()
    if task.state == 'SUCCESS':
        celery_status = 'Up'
    return celery_status
