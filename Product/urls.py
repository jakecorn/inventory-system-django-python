from django.conf.urls import url,include,url
from Product import views
urlpatterns = [
    url(r'^register/$', views.register, name='register_product'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^inventory/$', views.inventory, name='inventory'),
    url(r'^form/$', views.get_form, name='form'),
    url(r'^update/([0-9]+)/$', views.update, name='product_update'),

    url(r'^delete/(?P<product_id>\d+)/$', views.product_delete, name='product_delete'),

    url(r'^supplier/register/$', views.supplier_register, name='supplier_register'),
    url(r'^supplier/$', views.supplier_list, name='supplier_list'),
    url(r'^supplier/delete/([0-9]+)$', views.supplier_delete, name='supplier_delete'),
    url(r'^supplier/update/([0-9]+)$', views.supplier_update, name='supplier_update'),
    

    # url(r'^user/update/(?P<user_id>\d+)/$', 'User.views.user_update', name='user_update'),
    # url(r'^user/update/(?P<user_id>\d+)/submit/$', 'User.views.user_update_submit'),

]