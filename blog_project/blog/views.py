from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required, permission_required

def post_list(request):
    posts = Post.objects.filter(published = True)
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not post.published and not request.user.has_perm('blog.can_publish_post'):
        return render(request, 'blog/access_denied.html')
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
@permission_required('blog.add_post', raise_exception = True)
def post_create(request):
    if request.method == " POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail.html',pk = post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})
    
