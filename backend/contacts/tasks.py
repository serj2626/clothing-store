from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_message(name, email, message):
    send_mail(
        subject="Обратная связь",
        message=f"Имя: {name}\nEmail: {email}\nСообщение: {message}",
        from_email="q0k7I@example.com",
        recipient_list=["q0k7I@example.com"],
    )
    return {"status": "success", "message": "Сообщение успешно отправлено"}
