from django.shortcuts import render

# Create your views here.
def get_homepage(request):
    return render(request, 'homepage.html',context={})
def get_write(request):
    return render(request, 'writepage.html',context={})
def save_blog(request):
    title = request.POST['title']
    content = request.POST['content']
    author = request.POST['author']
    print("SAVED")
    blog = Blogs(title=title,content=content,author=author)
    blog.save()
    return redirect("write")
def show_all(request):
    blog=Blogs.objects.all()
    context={
        'blogs':blog
    }
    return render(request, 'allblogs.html',context=context)
def get_one_blog(request,bid):
    blog=Blogs.objects.get(pk=bid)
    context={
        'onlyblog':blog
    }
    return render(request,'singleblog.html',context=context)
def delete_blog(request,bid):
    blog=Blogs.objects.filter(pk=bid)
    blog.delete()
    return redirect("all")
def updateblog(request,bid):
    blog=Blogs.objects.get(pk=bid)
    context={
        'blogs':blog
    }
    print(context)
    return render(request,'updateblog.html',context=context)
def update_blog(request,bid):
    blog=Blogs.objects.get(pk=bid)
    blog.title = request.POST['title']
    blog.content = request.POST['content']
    blog.author = request.POST['author']
    blog.save()
    return redirect("all")
