from rest_framework.routers import SimpleRouter
from .views import ItemsPage , OrderAdd
from django.urls import path

router = SimpleRouter()
router.register('api/items', ItemsPage) #помещяем новый URL адресс который будем отслеживать


urlpatterns = [
    path('api/order-add/', OrderAdd.as_view())
]
urlpatterns +=router.urls

