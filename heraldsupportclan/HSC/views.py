from multiprocessing import context
from turtle import pos, title
from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, EventReview, LatestEvents, Post, slider, review,  Eventslider, Eventabout, Category, ForumPost,Comment,Reply,Gallery
from django.views.generic import ListView
from .utils import update_views
from .forms import UpdateForm,ForumPostForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage




# Create your views here.

def registerPage(request):
    context ={}
    return render(request,'registration/register.html', context)

def loginPage(request):
    context ={}
    return render(request,'registration/login.html', context)
    
def ForgotPassword(request):
    return render(request, 'ForgotPassword.html')

def update_profile(request):
    context={}
    return render(request,'update.html',context)

def Home(request):
   secs = LatestEvents.objects.all()
   students= review.objects.all()
   return render(request,'Home.html', {
       'secs': secs,
       'students':students,
   })  

def Forums(request):
    forums = Category.objects.all()
    num_posts = ForumPost.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = forums.count()
    last_post = ForumPost.objects.latest("date")


    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_users":num_users,
        "num_categories":num_categories,
        "last_post":last_post
    }
    return render(request,'Forums.html',context)

def detail(request, slug):
    post = get_object_or_404(ForumPost, slug=slug)
    author = Author.objects.get(user=request.user)

    if "comment-form" in request.POST:
       comment = request.POST.get("comment")
       new_comment, created  = Comment.objects.get_or_create(user=author, content=comment)
       post.comments.add(new_comment.id)
    
    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        comment_id = request.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=comment_id)
        new_reply, created = Reply.objects.get_or_create(user=author, content=reply)
        comment_obj.replies.add(new_reply.id)

    context={
        "post":post,
        "title":post.title,
    }
    update_views(request, post)

    return render(request,'detail.html', context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = ForumPost.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    context = {
        "posts":posts,
        "forum": category,
        "title": "Posts",
    }
    return render(request,'posts.html',context)



def Event(request):
    eventslider= Eventslider.objects.all()
    eventabout= Eventabout.objects.all()
    eventreview = EventReview.objects.all()
    eventgallery = Gallery.objects.all()
    return render(request,'Event.html',{
        'eventslider':eventslider,
        'eventabout': eventabout,
        'eventreview': eventreview,
        'eventgallery': eventgallery,
        })

def gallery(request):
    return render(request,'gallery.html')


def changepassword(request):
    return render(request, 'change-password.html')

def eventinfo(request):
    sliderdata = slider.objects.all()
    return render(request,'eventinfo.html',{'sliderdata':sliderdata})

def studentreview(request):
    students= review.objects.all()
    return render(request, 'studentreview.html',{'students': students})

class Newsletter(ListView):
    model = Post
    template_name = 'Newsletter.html'
    ordering = ['-post_date']

def update_profile(request):
    context = {}
    user = request.user 
    form = UpdateForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            update_profile = form.save(commit=False)
            update_profile.user = user
            update_profile.save()
            return redirect("Home")

    context.update({
        "form": form,
        "title": "Update Profile",
    })
    return render(request, "update.html", context)

def create_post(request):
    context = {}
    form = ForumPostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            return redirect("Forums")
    context.update({
        "form" : form,
        "title" : "Create New Post"
    })
    return render(request, "create_post.html" , context)

def latest_posts(request):
    posts = ForumPost.objects.all().filter(approved=True)[:10]
    context = {
        "posts": posts,
        "title": "Latest 10 Posts"
    }

    return render(request, "latest-posts.html",context)

def search_result(request):
    return render(request,"search.html")


def team(request):
    return render(request, "team.html")










