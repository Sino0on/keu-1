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
        context['categories'] = Category.objects.filter(head_category__isnull=True)
        context['head_categories'] = HeadCategory.objects.all()
        context['programs'] = Program.objects.all()
        context['aboutkeus'] = AboutCategory.objects.all()
        context['pages'] = BlankPage.objects.all()
        context['news'] = News.objects.order_by('-date')[:3]
        context['abouts'] = About.objects.all()
        context['aboutkeu'] = AboutKEU.objects.all()[0]
        return context
class NewsListView(ListView):
    model = News
    queryset = News.objects.all()
    context_object_name = 'news'
    template_name = 'news.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['categories'] = Category.objects.filter(head_category__isnull=True)
        context['head_categories'] = HeadCategory.objects.all()
        context['programs'] = Program.objects.all()
        context['aboutkeus'] = AboutCategory.objects.all()
        context['aboutkeu'] = AboutKEU.objects.all()[0]
        context['abouts'] = About.objects.all()
        return context


class DetailNews(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'detail_news.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['categories'] = Category.objects.filter(head_category__isnull=True)
        context['head_categories'] = HeadCategory.objects.all()
        context['programs'] = Program.objects.all()
        context['aboutkeus'] = AboutCategory.objects.all()
        context['aboutkeu'] = AboutKEU.objects.all()[0]
        context['abouts'] = About.objects.all()
        return context


class ProgramListView(ListView):
    model = Program
    queryset = Program.objects.all()
    context_object_name = 'programs'
    template_name = 'programs.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['categories'] = Category.objects.filter(head_category__isnull=True)
        context['head_categories'] = HeadCategory.objects.all()
        context['programs'] = Program.objects.filter(category__isnull=True)
        context['aboutkeus'] = AboutCategory.objects.all()
        context['news'] = News.objects.order_by('-date')[:3]
        context['aboutkeu'] = AboutKEU.objects.all()[0]
        context['abouts'] = About.objects.all()
        return context


class ProgramListByCategoryView(DetailView):
    model = ProgramCategory
    queryset = ProgramCategory.objects.all()
    context_object_name = 'programcategory'
    template_name = 'programs.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['categories'] = Category.objects.filter(category=context['programcategory'])
        context['head_categories'] = HeadCategory.objects.all()
        context['programs'] = Program.objects.filter(category__isnull=True)
        context['aboutkeus'] = AboutCategory.objects.all()
        context['news'] = News.objects.order_by('-date')[:3]
        context['aboutkeu'] = AboutKEU.objects.all()[0]
        context['abouts'] = About.objects.all()
        return context

class ProgramDetailView(DetailView):
    model = Program
    queryset = Program.objects.all()
    context_object_name = 'program'
    template_name = 'program_detail.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['categories'] = Category.objects.filter(head_category__isnull=True)
        context['head_categories'] = HeadCategory.objects.all()
        context['programs'] = Program.objects.all()
        context['aboutkeus'] = AboutCategory.objects.all()
        context['news'] = News.objects.order_by('-date')[:3]
        context['aboutkeu'] = AboutKEU.objects.all()[0]
        context['abouts'] = About.objects.all()
        return context


class ProjectListView(ListView):
    model = Project
    queryset = Program.objects.all()
    context_object_name = 'programs'
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['categories'] = Category.objects.filter(head_category__isnull=True)
        context['head_categories'] = HeadCategory.objects.all()
        context['programs'] = Program.objects.all()
        context['aboutkeus'] = AboutCategory.objects.all()
        context['aboutkeu'] = AboutKEU.objects.all()[0]
        context['news'] = News.objects.order_by('-date')[:3]
        context['abouts'] = About.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = Project
    queryset = Project.objects.all()
    context_object_name = 'project'
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['programs'] = Program.objects.all()
        context['categories'] = Category.objects.filter(head_category__isnull=True)
        context['head_categories'] = HeadCategory.objects.all()
        context['aboutkeus'] = AboutCategory.objects.all()
        context['news'] = News.objects.order_by('-date')[:3]
        context['aboutkeu'] = AboutKEU.objects.all()[0]
        context['abouts'] = About.objects.all()
        return context


class AboutKeuDetailView(DetailView):
    model = AboutKEU
    queryset = AboutKEU.objects.all()
    context_object_name = 'aboutpage'
    template_name = 'aboutKEUS.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['categories'] = Category.objects.filter(head_category__isnull=True)
        context['head_categories'] = HeadCategory.objects.all()
        context['programs'] = Program.objects.all()
        context['aboutkeus'] = AboutCategory.objects.all()
        context['news'] = News.objects.order_by('-date')[:3]
        context['aboutkeu'] = AboutKEU.objects.all()[0]
        context['abouts'] = About.objects.all()
        return context


class AboutDetailView(DetailView):
    model = About
    queryset = About.objects.all()
    context_object_name = 'aboutpage'
    template_name = 'aboutKEUS.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['categories'] = Category.objects.filter(head_category__isnull=True)
        context['head_categories'] = HeadCategory.objects.all()
        context['programs'] = Program.objects.all()
        context['aboutkeus'] = AboutCategory.objects.all()
        context['news'] = News.objects.order_by('-date')[:3]
        context['aboutkeu'] = AboutKEU.objects.all()[0]
        context['abouts'] = About.objects.all()
        return context


class PageDetailView(DetailView):
    model = BlankPage
    queryset = BlankPage.objects.all()
    context_object_name = 'aboutpage'
    template_name = 'aboutKEUS.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['programs'] = Program.objects.all()
        context['categories'] = Category.objects.filter(head_category__isnull=True)
        context['head_categories'] = HeadCategory.objects.all()
        context['aboutkeus'] = AboutCategory.objects.all()
        context['news'] = News.objects.order_by('-date')[:3]
        context['aboutkeu'] = AboutKEU.objects.all()[0]
        context['abouts'] = About.objects.all()
        return context

class Question(CreateView):
    model = Messages
    template_name = 'base.html'
    fields = '__all__'


def forum(request):
    documents = DocsForum.objects.all()
    return render(request, 'forum.html', {'documents': documents})


def document_detail(request, pk):
    document = Documents.objects.get(id=pk)
    return render(request, 'document_detail.html', {'document': document})
