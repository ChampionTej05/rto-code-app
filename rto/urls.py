from django.urls import path,re_path

from . import views
app_name = 'rto'
urlpatterns = [
    path('', views.home, name='home'),
    path('find',views.findCity,name='findCity'),
    # path('add',views.addCity,name='addCity'),
    path('findall',views.findAll,name='findAll'),
    re_path('^.*$',views.showError , name="showError")
]