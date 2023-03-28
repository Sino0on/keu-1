from django.conf import settings
from .views import *
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='home')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


