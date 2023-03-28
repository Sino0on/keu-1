from django.shortcuts import render
from .models import *

from django.views.generic import ListView, DetailView,CreateView

# def home(request):
#     return render(request,'index.html',{})

class Home(ListView):
    model = About
    queryset = About.objects.all()
    context_object_name = 'abouts'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['programs'] = Program.objects.all()
        context['aboutkeus'] = AboutKEU.objects.all()
        context['news'] = News.objects.order_by('-date')[:3]
        print(context['news'])
        return context
class NewsListView(ListView):
    model = News
    queryset = News.objects.all()
    context_object_name = 'news'
    template_name = 'news.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['programs'] = Program.objects.all()
        context['aboutkeus'] = AboutKEU.objects.all()
        context['abouts'] = About.objects.all()
        return context
class DetailNews(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'detail_news.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['programs'] = Program.objects.all()
        context['aboutkeus'] = AboutKEU.objects.all()
        context['abouts'] = About.objects.all()
        return context
