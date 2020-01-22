from django.conf.urls import url,include,url
from User import views
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^list/$', views.user_list, name='user_list'),
    url(r'^register/submit/$', views.register_submit,name="user_submit"),

    url(r'^delete/(?P<user_id>\d+)/$', views.user_delete, name='user_delete'),
    

    url(r'^update/(?P<user_id>\d+)/$', views.user_update, name='user_update'),
    url(r'^update/(?P<user_id>\d+)/submit/$', views.user_update_submit),

]