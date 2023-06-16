from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='sginup'),
    path('success/', views.success_page, name='vio'),
]