from django.urls import path
from .import views 
#from .views import index, ebayindex

urlpatterns = [

    path('amazon', views.amazon, name='amazon'),
    path('ebay', views.ebay, name='ebay'),
    path('<int:id>/', views.product_detail, name="product_detail"),
]