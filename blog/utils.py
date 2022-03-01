from django.core.paginator import Paginator

def pagination(request, obj, number_of_article_per_page=5):
    paginator = Paginator(obj, number_of_article_per_page)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj