
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article

# Create your views here.
@permission_required('app_name.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})
@permission_required('app_name.can_create', raise_exception=True)
def article_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Article.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        return redirect('article_list')

    return render(request, 'articles/create.html')
@permission_required('app_name.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect('article_list')

    return render(request, 'articles/edit.html', {'article': article})
@permission_required('app_name.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')
