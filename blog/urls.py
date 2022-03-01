from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-category', views.all_article),
    path('article/search/', views.search, name='search'),
    
    path('article/<int:id>/', views.article, name='article'),
    path('article/category/<str:category_name>/', views.article_by_category, name='categorie'),
]