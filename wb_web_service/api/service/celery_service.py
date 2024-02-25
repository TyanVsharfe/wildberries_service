import os
import time

from celery import Celery
from celery.utils.log import get_task_logger

from wb_web_service.api.service.product_service import update_all_products
from wb_web_service.config import settings

logger = get_task_logger(__name__)
celery = Celery(__name__)
celery.conf.broker_url = settings.CELERY_BROKER_URL
celery.conf.result_backend = settings.CELERY_RESULT_BACKEND


@celery.task(name="update_all_products_task")
def update_all_products_task():
    time.sleep(5)
    update_all_products()
    logger.info("All products updated")
