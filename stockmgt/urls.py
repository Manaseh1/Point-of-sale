from django.urls import path
from .views import stock_alerts,restock,stock

appname  = 'stockmgt'
urlpatterns = [
    path('stock-alerts/', stock_alerts, name='stock_alerts'),
    path('stock/', stock, name='stock'),

    path('restock/<int:stock_id>/', restock, name='restock')
]
