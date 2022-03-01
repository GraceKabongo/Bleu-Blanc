from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Article, Category
from .utils import pagination


def index(request):
    articles = Article.objects.all().order_by('-created_at')
    page_obj = pagination(request, articles)
    return render(request, template_name='blog/index.html', context={'page_obj': page_obj})


def article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, template_name='blog/article.html', context={'article' : article})


def article_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name.lower())    
    articles = Article.objects.filter(category=category).all().order_by('-created_at')
    
    page_obj = pagination(request, articles)  
    return render(request, template_name='blog/index.html', context={'page_obj': page_obj, 'title' : category_name})

def all_article(request):
    categories = Category.objects.all()
    data = []
    for category in categories:
        data.append(category.name)
    return JsonResponse({'category' : data})
    

def search(request):
    search = request.GET
    context = {}
    
    if search and search['search']:
        articles = Article.objects.filter(title__icontains=search['search']).order_by('-created_at').all()
        
        if articles.exists():
            page_obj = pagination(request, articles)
            context['page_obj'] = page_obj
            context['query'] = search['search']
        else:
            context['is_empty'] = True

    return render(request, template_name='blog/search.html', context=context)
