from django.shortcuts import render,redirect

# Create your views here.


#from django.http import HttpResponse
from .models import Comment

from .forms import CommentForm


def index(request):
    comments = Comment.objects.order_by('-date')
    context = {'comments':comments}
    return render(request,'index.html',context)

def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment  = Comment(name=request.POST['name'],message=request.POST['message'])
            new_comment.save()
            return redirect('index')
    else:

        form = CommentForm()
    context = {'form':form}
    return render(request,'sign.html',context)
