from HSC.models import ForumPost


def searchFunction(request):
    search_context = {}
    posts = ForumPost.objects.all()
    if "search" in request.GET:
        query = request.GET.get("q")
        #Filter start here 
        search_box = request.GET.get("search-box")
        if search_box == "Descriptions":
            objects = posts.filter(content__icontains=query)
        else:
            objects = posts.filter(title__icontains=query)
        #ends here
        for obj in objects:
            print(obj.title)
        search_context = {
            "objects" : objects,
            "query" : query,
        }
    
    return search_context