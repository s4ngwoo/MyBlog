from django.urls import path
from . import views

app_name="myblog"

urlpatterns = [
    path('', views.landing, name="landing"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('archive/', views.archive, name="archive"),
    path('archive/<int:pk>', views.post, name="post"),
]