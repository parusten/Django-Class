from django.contrib import admin
from django.urls import path
# from app1.views import hello,hello1,hello2,greet,index
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dola/',views.hello),
    path('name/',views.hello1),
    path('address/',views.hello2),
    path('greet/<str:name>/',views.greet),
    path('',views.index),
    path('send', views.send),

]
