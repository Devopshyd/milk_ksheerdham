from django.urls import path
from App import views

urlpatterns = [
    path('',views.product_view,name='products1'),
    path('getdata',views.total_data,name='getdata'),
    path('onedata',views.OneData,name='onedata'),
    path('farmdata',views.Farm_Data,name='farmdata'),
]
