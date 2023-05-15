from datetime import time

from .serializers import ItemSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from cloudipsp import Api, Checkout



class ItemsPage(ModelViewSet):
    queryset = Item.objects.all() # Говорим что конкретно будем выбирать
    serializer_class = ItemSerializer

class OrderAdd(APIView):
    def post(self, req): # название метода можно менять в зависимости от требований
        order = OrderSerializer(data=req.data)
        if order.is_valid():
            order.save()
            api = Api(merchant_id=1396424,
                      secret_key='test')
            checkout = Checkout(api=api)
            data = {
                "currency": "USD",
                "amount": int(req.data['summa'])*100,
                "order_desc": "Оплата товара",

            }
            url = checkout.url(data).get('checkout_url')


            return Response({'result': 'Пару секунд...', 'url' : url})

        return Response({'result': 'Ошибка в форме'})

