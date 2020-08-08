from django.contrib import admin
from django.urls import path,include
from newsletter import urls as newsletter_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(newsletter_urls, namespace="newsletter")),
]
