from django.shortcuts import render


# Create your views here.
def blog(request):
    blog = blog.objects.all()
    return render(request,"blog/blog.html",{"blog": blog})