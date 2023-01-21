
from django.urls import path
from .import views

app_name = 'user_shop'
urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('filter/', views.filter_price, name='filter_price'),
    path('<slug:c_slug>/', views.allProdCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]