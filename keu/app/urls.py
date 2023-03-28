from django.conf import settings
from .views import *
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('news/', DetailNews.as_view(), name='news'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


