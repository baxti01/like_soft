from celery import shared_task
from django.core.mail import send_mail, BadHeaderError

from like_soft import settings


@shared_task
def send_email_task(username, email):
    subject = f'{username} - Добро пожаловать в систему Like Soft'
    message = ('Благодарим за регистрацию в нашем сервисе.\n'
               ' Чтобы пользоваться ей дальше, перейдите в сайт '
               'и создавайте, читайте или редактируйте ваши книги')
    try:
        send_mail(
            subject=subject,
            from_email=settings.DEFAULT_FROM_EMAIL,
            message=message,
            recipient_list=[email]
        )
    except BadHeaderError:
        return 'Invalid header error'

    return 'Email success sent'
