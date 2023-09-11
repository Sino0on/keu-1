from django.conf import settings
from .views import *
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', DetailNews.as_view(), name='detail_news'),
    path('program/list', ProgramListView.as_view(), name='programs'),
    path('project/list', ProjectListView.as_view(), name='projects'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('aboutKEU/<int:pk>', AboutKeuDetailView.as_view(), name='aboutkeu_detail'),
    path('about/<int:pk>', AboutDetailView.as_view(), name='about_detail'),
    path('page/<int:pk>', PageDetailView.as_view(), name='page_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('send_question', Question.as_view(), name='question'),
    path('forum', forum, name='forum')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
