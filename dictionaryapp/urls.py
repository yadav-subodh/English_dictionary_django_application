from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('contact', views.contact),
    path('search', views.search),
    path('adminPage', views.admin_page),
    path('adminLogin', views.admin_login),
    path('wordPage', views.word),
    path('home', views.home),
    path('submitContact', views.submit_contact_details),
    path('submitWord', views.add_word),

]
