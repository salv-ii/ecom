from ecom import settings
from django.conf.urls.static import static

from . import views
from django.urls import path, include
app_name='ecom_app'
urlpatterns = [

    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetails, name='prodCatdetail'),

]

