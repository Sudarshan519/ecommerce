from django.shortcuts import render,redirect
from .models import Blogpost,Post,BlogComment
from django.contrib import messages
# Create your views here.
def index(request):
    mypost=Post.objects.all()
    #print(mypost)
    return render(request, 'blog/index.html',{'allPost':mypost})

def blogpost(request,slug):
   
    post=Post.objects.filter(slug = slug).first()
    #print(post)
    comments=BlogComment.objects.filter(post=post)
    context={'post':post,'comments':comments}
    return render(request, 'blog/blogpost.html',context)

def postComment(request):
    if request.method == "POST":
        print('post')
        comment=request.POST.get('comment')
        user=request.user
        postSno=request.POST.get('postSno')
        post=Post.objects.get(sno=postSno)
        comment=BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,"You have successfully commented on post")    
    return redirect(f'/blog/{post.slug}')
    