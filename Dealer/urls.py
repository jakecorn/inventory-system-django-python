from django.conf.urls import url,include,url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='dealer_list'),
    url(r'^register/$', views.register, name='register_dealer'),
    url(r'^register/update/([0-9]+)$', views.dealer_update, name='dealer_update'),

    url(r'^register/delete/([0-9]+)$', views.dealer_delete, name='dealer_delete'),

    url(r'^id/([0-9]+)/order/add/$', views.add_order, name='add_order'),
    url(r'^order/save/$', views.save_order, name='save_order'),

]