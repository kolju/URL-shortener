from django.shortcuts import render, redirect
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from url_shortener.forms import LinkShortenerForm
from .models import Link


def index(request):
    if request.method == 'POST':
        form = LinkShortenerForm(request.POST)
        if form.is_valid():
            url = {'long_url': form.cleaned_data['url']}
            link = Link.objects.create(**url)
            return redirect('info/%s' % str(link.id))
    else:
        form = LinkShortenerForm()
        top_url = Link.objects.all().order_by('-clicks_count', '-created')[:20]
    return render(request, 'url_shortener/index.html', {'form': form, 'top_url': top_url})


def info(request, link_id):
    url = Link.objects.get(id=link_id)
    return render(request, 'url_shortener/info.html', {'url': url})


def url_redirect(request, short):
    obj = Link.objects.get(short=short)
    obj.clicks_count = F('clicks_count') + 1
    obj.save()
    return redirect(obj.long_url)


def delete_obj(request, link_id):
    if request.method == 'POST':
        Link.objects.filter(id=link_id).delete()
    return redirect('/shortener/overall/')


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