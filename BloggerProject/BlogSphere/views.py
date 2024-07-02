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
