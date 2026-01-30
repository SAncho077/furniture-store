from django.db import models


class News(models.Model):
    CATEGORY_CHOICES = [
        ('news', 'Новости компании'),
        ('promo', 'Акции и скидки'),
        ('event', 'Мероприятия'),
        ('tips', 'Советы по уходу'),
        ('new', 'Новинки'),
    ]

    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    short_description = models.CharField('Краткое описание', max_length=300, blank=True)
    image = models.ImageField('Изображение', upload_to='news', blank=True)
    read_time = models.IntegerField('Время чтения (мин)', default=5)
    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOICES, default='news')
    published_date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
