from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, EventGalleryCategory, review, EventGalleryPictures, EventReview, LatestEvents, Post, slider,  Eventslider, Eventabout, Category, ForumPost,Comment,Reply,Gallery, Notify,NotifUserStatus
from django.views.generic import ListView, CreateView
from .utils import update_views
from .forms import UpdateForm,ForumPostForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse


# Create your views here.

def registerPage(request):
    context ={}
    return render(request,'registration/register.html', context)

def loginPage(request):
    context ={}
    return render(request,'registration/login.html', context)
    
def ForgotPassword(request):
    return render(request, 'ForgotPassword.html')


def Home(request):
   secs = LatestEvents.objects.all()
#    students= review.objects.all()
   return render(request,'Home.html', {
       'secs': secs,
       'room_name': "broadcast"
    
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
    eventtitle = EventGalleryCategory.objects.all()
    eventimage = EventGalleryPictures.objects.all()
    return render(request,'gallery.html',{
        'eventtitle': eventtitle,
        'eventimage' : eventimage,

    })


def changepassword(request):
    return render(request, 'change-password.html')

def eventinfo(request):
    sliderdata = slider.objects.all()
    return render(request,'eventinfo.html',{'sliderdata':sliderdata})

# def studentreview(request):
#     students= studentreview.objects.all()
#     return render(request, 'studentreview.html',{'students':students})

class Newsletter(ListView):
    model = Post
    template_name = 'Newsletter.html'
    ordering = ['-post_date']
    
def studentreview(request):
    students= review.objects.all()
    return render(request, 'studentreview.html',{'students': students})

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
            form.save_m2m()
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

def Forum_postsapproval(request):
    Forum_post_list = ForumPost.objects.all().order_by('-date')
    if request.user.is_superuser:
        if request.method == "POST":
            id_list = request.POST.getlist('boxes')
            #update database
            for x in id_list:
                ForumPost.objects.filter(pk=int(x)).update(approved=True)

            messages.success(request,("Forum Posts Approval Has Been Updated!"))
            return redirect('Forums')

        else:
            return render(request,'Forum_postsapproval.html',{'Forum_post_list':Forum_post_list})
    else:
        messages.success(request,("You are not authorized to view this page"))
        return redirect('Home')

# Notifications
def notifications(request):
    data= Notify.objects.all().order_by('-id')
    return render(request, "notifications.html",{'data':data})

#Get Notifications
def getnotifications(request):
   data= Notify.objects.all().order_by('-id')
   notifStatus=False
   jsonData=[]
   totalUnread=0
   for d in data:
      
      try:
          notifStatusData=NotifUserStatus.objects.get(user=request.user,notif=d)

          if notifStatusData:
            notifStatus=True
      except NotifUserStatus.DoesNotExist:
          notifStatus=False
      if not notifStatus:
          totalUnread=totalUnread+1
      jsonData.append({
           'pk':d.id,
           'notify_detail':d.notify_detail,
           'notifStatus':notifStatus
        })

   #jsonData=serializers.serialize('json',data)
   return JsonResponse({'data':jsonData,'totalUnread':totalUnread})

#Mark Read By user
def mark_read_notif(request):
    notif=request.GET['notif']
    notif=Notify.objects.get(pk=notif)
    user=request.user
    NotifUserStatus.objects.create(notif=notif, user=user, status=True)
    return JsonResponse({'bool':True})


