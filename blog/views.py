from django.shortcuts import render,get_object_or_404,HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
# Create your views here.
def init(request):
    return render(request,'blog/blog_init.html')
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":#检查html里的method
        form = PostForm(request.POST)
        if form.is_valid():#提交了表单之后
            post = form.save(commit=False)#commit=False意味着我们还不想保存Post模型—我们想首先添加作者
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})