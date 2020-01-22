from django.conf.urls import url,include,url
from Cashier import views
urlpatterns = [
    url(r'^home/$', views.cashier_home, name='cashier_home'),
    url(r'^product/search/$', views.search_product, name='search_product'),
    url(r'^order/save/$', views.save_order),

]