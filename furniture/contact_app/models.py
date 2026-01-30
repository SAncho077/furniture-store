from django.db import models
from django.utils import timezone


class ContactRequest(models.Model):



    name = models.CharField(
        'Имя',
        max_length=100
    )

    phone = models.CharField('Телефон', max_length=20)
    question = models.TextField('Вопрос', blank=True)
    agree_to_processing = models.BooleanField(
        'Согласие на обработку',
        default=False
    )


    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('processed', 'Обработана'),
        ('rejected', 'Отклонена'),
    ]
    status = models.CharField(
        'Статус',
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    processed_at = models.DateTimeField('Обработано', null=True, blank=True)

    # ======== МЕТАДАННЫЕ ========
    class Meta:
        verbose_name = 'Заявка на контакт'
        verbose_name_plural = 'Заявки на контакт'
        ordering = ['-created_at']


    def __str__(self):
        return f'{self.name} - {self.phone} - {self.created_at}'