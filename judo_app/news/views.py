from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import NewsForm
from django.utils import timezone

# Create your views here.


def NewsView(request, *args, **kwargs):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})


def News_DetailView(request, pk, *args, **kwargs):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news': news})


def News_NewView(request, *args, **kwargs):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news-detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news_edit.html', {'form': form})


def News_Edit(request, pk, *args, **kwargs):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.edited = timezone.now()
            news.save()
            return redirect('news-detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news_edit.html', {'form': form})
