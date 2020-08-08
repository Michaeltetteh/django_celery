from django.urls import path, include
from .views import newsletter_view

app_name = "newsletter"


urlpatterns = [
    path('',newsletter_view,name="newsletter-view"),
]
