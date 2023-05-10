from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article, Comment
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        context = {
            "articles":articles,
        }
    
        return render(request, "articles.html", context)
    else:
        articles = Article.objects.all()

        context = {
            "articles":articles,
        }
        
        return render(request, "articles.html", context)


@login_required(login_url="user:login")
def deleteArticle(request, id):
    article =  get_object_or_404(Article, id=id)
    article.delete()

    messages.success(request, "Successfully Deleted.")
    
    return redirect("article:dashboard")
    

@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False) #forbit save() to save article without author
        article.author = request.user #assign an author
        article.save()
        
        messages.success(request, "Article Updated")
        
        return redirect("article:dashboard")
    else:    
        context = {
            "form":form,
        }
     
        return render(request, "update.html", context) 

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    
    context = {
        "articles":articles,
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit=False) #forbit save() to save article without author
        article.author = request.user #assign an author
        article.save()
        
        messages.success(request, "Article Added")
        
        return redirect("index")
    else:    
        context = {
            "form":form,
        }
        return render(request, "addarticle.html", context)


def detail(request, id):
    """this is how we make a function which include a dynamic link"""
    #article = Article.objects.get(id = id)
    article = get_object_or_404(Article, id=id)
    
    comments = article.comments.all()
    context= {
        "article":article,
        "comments":comments,
    }
    return render(request, "detail.html", context)



def addComment(request, id):
    article = get_object_or_404(Article, id=id)
    
    if request.method == "POST":
        comment_author  = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        
        new_comment = Comment(comment_author=comment_author, comment_content=comment_content)
        new_comment.article = article
        new_comment.save()
        
    return redirect("article:detail", id)