from django.conf import settings
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.contrib.auth.signals import user_logged_in
import logging

logger = logging.getLogger(__name__)
User = get_user_model()


@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
    if created:

        subject = f"Добро пожаловать в мебельный мир, {instance.first_name}!"
        message = f"""Уважаемый(ая) {instance.first_name} {instance.last_name},

        Поздравляем с успешной регистрацией в интернет-магазине «Furniture»!

        Теперь вам доступны:
        ✅ Быстрое оформление заказов
        ✅ История ваших покупок
        ✅ Отслеживание статуса заказа
        ✅ Персональные скидки и акции
        ✅ Сохранение избранных товаров
        ✅ Быстрый повторный заказ

        Создайте уют в вашем доме с нашей мебелью:
        • Гостиные и спальни
        • Кухни и столы
        • Офисная мебель
        • Детские комнаты
        • Шкафы и системы хранения


        Желаем приятных покупок!

        С уважением,
        Команда мебельного магазина «Furniture»
  
        """

        from_email = settings.EMAIL_HOST_USER
        to_email = instance.email

        try:
            send_mail(
                subject,
                message,
                from_email,
                [to_email],
                fail_silently=False,
            )
            logger.info(f"Письмо приветствия отправлено на {to_email}")
        except Exception as e:
            logger.error(f"Ошибка отправки письма при регистрации: {e}")


@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):

    subject = f"С возвращением в мир уюта, {user.first_name}!"
    message = f"""Здравствуйте, {user.first_name} {user.last_name}!

    Рады снова видеть вас в нашем мебельном магазине «Ваш Дом»!

    Ваш последний визит: {user.last_login.strftime('%d.%m.%Y в %H:%M')}"""

    from_email = settings.EMAIL_HOST_USER
    to_email = user.email

    try:
        send_mail(
            subject,
            message,
            from_email,
            [to_email],
            fail_silently=False,
        )
        logger.info(f"Письмо при входе отправлено на {to_email}")
    except Exception as e:
        logger.error(f"Ошибка отправки письма при авторизации: {e}")