from django.urls import path
from orders.views import OrderCreateView, full_order, OrderListView

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name="order-create"),
    path('full-order-/', full_order, name="full-order"),


]