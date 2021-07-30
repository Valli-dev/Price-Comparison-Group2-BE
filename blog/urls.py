from django.urls import path
from .import views 
from .views import like_view, get_product,details, compare_price
urlpatterns = [
        
        path('', get_product, name='homeview'),
        path('details/<int:id>',details,name='product-detailsview'),
        path('like/',like_view, name='like_product'),
        path('compare_price/', compare_price, name='compare_price'),



]