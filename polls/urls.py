from django.urls import path
from . import views

#URLconfiguration
urlpatterns = [
    path('hello/', views.say_hello),
    #path('hello/pdf', views.generate_pdf)
]