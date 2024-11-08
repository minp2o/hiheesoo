
from django.contrib import admin
from django.urls import path
from . import views

app_name='myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AB/',views.file_open_by_numpy,name = 'AB'),
    path('C/',views.average_ten,name = 'C')
    
]
