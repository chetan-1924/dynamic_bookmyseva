from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about_us_page, name="about"),
    path('contact/', views.contact, name="contact"),
    path('pricing/', views.pricing, name="pricing"),
    path('service/', views.service, name="service")
]
# urlpatterns = [path("about/", views.about, name="about")]
# urlpatterns = [path("/contact", views.contact, name="contact")]