from django.conf import settings
from .views import *
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('program/list', ProgramListView.as_view(), name='programs'),
    path('project/list', ProjectListView.as_view(), name='projects'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('news/', DetailNews.as_view(), name='news'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



