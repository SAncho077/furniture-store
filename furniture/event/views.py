from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import News


def news_list(request):
    all_news = News.objects.all().order_by('-published_date')

    paginator = Paginator(all_news, 6)
    page = request.GET.get('page', 1)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = {'news': news, 'title': 'События'}

    return render(request, 'event/news_list.html', context)


def news_detail(request, pk):
    product_obj = News.objects.get(id=pk)
    context = {
        "title": product_obj.title,
        'new': product_obj,
    }
    return render(request, 'event/new_detail.html', context)