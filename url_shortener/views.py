from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from url_shortener.forms import LinkShortenerForm
from .models import Link


def index(request):
    if request.method == 'POST':
        form = LinkShortenerForm(request.POST)
        if form.is_valid():
            link = form.save()

            return redirect('url_shortener:info', link_id=link.id)
    else:
        form = LinkShortenerForm()

    top_links = Link.objects.all().order_by('-clicks_count', '-created')[:20]

    return render(request, 'url_shortener/index.html', {'form': form, 'top_links': top_links})


def info(request, link_id):
    link = get_object_or_404(Link, id=link_id)

    return render(request, 'url_shortener/info.html', {'link': link})


def url_redirect(request, short_url):
    link = get_object_or_404(Link, short_url=short_url)
    link.clicks_count = F('clicks_count') + 1
    link.save()

    return redirect(link.long_url)


def delete_obj(request, link_id):
    if request.method == 'POST':
        Link.objects.filter(id=link_id).delete()

    return redirect('url_shortener:overall')


def overall(request):
    link_list = Link.objects.all().order_by('-clicks_count', '-created')
    paginator = Paginator(link_list, 10)

    page = request.GET.get('page', 1)
    try:
        links = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        raise Http404()

    return render(request, 'url_shortener/overall.html', {'links': links})
