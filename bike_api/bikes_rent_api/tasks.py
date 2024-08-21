from users_api.models import CustomUser
from bikes_rent_api.models import Rent
from celery import shared_task
from bike_api.settings import Tariff_rent
from datetime import datetime


@shared_task
def reprocessed(user_id, rent_id):
    user = CustomUser.objects.get(id=user_id)
    rent = Rent.objects.get(id=rent_id)
    delta_time = (rent.date_end - rent.date_start).total_seconds()
    user.wallet += delta_time * Tariff_rent
    user.save(update_fields=['wallet'])
