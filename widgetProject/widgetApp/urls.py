from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('residency_application/', views.residency_application, name='residency_application'),
    path('thankyou_page/', views.thankyou_page, name='thankyou_page'),

]
