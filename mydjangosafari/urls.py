from django.urls import path
from mydjangosafari import views
urlpatterns = [
    path('welcome/', views.karibu),
    path('', views.homepage, name='my_homepage'),
    path('about/', views.about, name='my_about'),
    path('contact/', views.contact, name='my_contact'),
    path('gallery/', views.gallery, name='my_gallery'),
    path('services/', views.services, name='my_services'),
]