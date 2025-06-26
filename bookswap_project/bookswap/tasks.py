from celery import shared_task
from django.core.mail import send_mail
from bookswap.models.user_models import User
from django.conf import settings

@shared_task
def send_user_list_email():
    users = User.objects.all()
    user_data = "\n".join([f"{user.username} - {user.email}" for user in users])

    send_mail(
        subject="Kullanıcı Listesi",
        message=user_data,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['kutayyildirim688@gmail.com'],
        fail_silently=False,
    )