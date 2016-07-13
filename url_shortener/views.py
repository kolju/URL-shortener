from django.shortcuts import render, redirect
from django.db.models import F
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
        top_url = Link.objects.all().order_by('-clicks_count')[:20]
    return render(request, 'url_shortener/index.html', {'form': form, 'top_url': top_url})


def info(request, link_id):
    url = Link.objects.get(id=link_id)
    return render(request, 'url_shortener/info.html', {'url': url})


def overall(request):
    objects_list = Link.objects.all()
    return render(request, 'url_shortener/overall.html', {'objects_list': objects_list})


def url_redirect(request, short):
    obj = Link.objects.get(short=short)
    obj.clicks_count = F('clicks_count') + 1
    obj.save()
    return redirect(obj.long_url)


def delete_obj(request, link_id):
    Link.objects.filter(id=link_id).delete()
    return redirect('/shortener/overall/')