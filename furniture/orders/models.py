from django.db import models
from users.models import User
from products.models import Basket


class Order(models.Model):
    CREATED = 0 # в корзине
    PAID = 1 # оплачен
    ON_WAY = 2 # в пути
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'в пути'),
        (DELIVERED, 'Доставлен'),
    )

    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(max_length=200, verbose_name="Email")
    address = models.CharField(max_length=250, verbose_name="Адрес")
    basket_history = models.JSONField(default=dict, verbose_name="История заказов")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.SmallIntegerField(choices=STATUSES, default=CREATED)
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик')

    def __str__(self):
        return f"Заказ #{self.id}. {self.first_name} {self.last_name}"

    def update_after_payment(self):
        baskets = Basket.objects.filter(user=self.initiator)
        self.status = self.PAID
        self.basket_history = {
            'purchased_items': [basket.de_json() for basket in baskets],
            'total_sum': float(baskets.total_sum())
        }
        baskets.delete()
        self.save()


    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"