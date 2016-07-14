from django.shortcuts import render, redirect
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from url_shortener.forms import LinkShortenerForm
from .models import Link


def index(request):
    if request.method == 'POST':
        form = LinkShortenerForm(request.POST)
        if form.is_valid():
            long_url = {'long_url': form.cleaned_data['url']}
            link = Link.objects.create(**long_url)
            return redirect('info', link_id=link.id)
    else:
        form = LinkShortenerForm()
        top_links = Link.objects.all().order_by('-clicks_count', '-created')[:20]
    return render(request, 'url_shortener/index.html', {'form': form, 'top_links': top_links})


def info(request, link_id):
    link = Link.objects.get(id=link_id)
    return render(request, 'url_shortener/info.html', {'link': link})


def url_redirect(request, short_url):
    link = Link.objects.get(short_url=short_url)
    link.clicks_count = F('clicks_count') + 1
    link.save()
    return redirect(link.long_url)


def delete_obj(request, link_id):
    if request.method == 'POST':
        Link.objects.filter(id=link_id).delete()
    # return redirect(request, 'url_shortener/overall.html')
    return redirect('/shortener/overall') #TODO: fix it


def overall(request):
    link_list = Link.objects.all().order_by('-clicks_count', '-created')
    paginator = Paginator(link_list, 10) # Show 10 links per page

    page = request.GET.get('page')
    try:
        links = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        links = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        links = paginator.page(paginator.num_pages)

    return render(request, 'url_shortener/overall.html', {'links': links})