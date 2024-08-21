from users_api.models import CustomUser
from celery import shared_task


@shared_task
def reprocessed(user: CustomUser):
    f = CustomUser.objects.get(id=user.id)
    f.save()
