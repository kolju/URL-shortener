from django.shortcuts import render, redirect
from url_shortener.forms import LinkShortenerForm
from .models import Link


def index(request):
    if request.method == 'POST':
        form = LinkShortenerForm(request.POST)
        if form.is_valid():
            url = {'long_url': form.cleaned_data['url']}
            # url = form.cleaned_data['url']
            link = Link.objects.create(**url)
            return redirect('info')
    else:
        form = LinkShortenerForm()
        top_url = Link.objects.all().order_by('-clicks_count')[:20]
    return render(request, 'url_shortener/index.html', {'form': form, 'top_url': top_url})


def info(request, link_id):
    return render(request, 'url_shortener/info.html', {'link': link_id})

