from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404

def Post_list(request):
    Posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/Post_list.html', {'Posts': Posts}) 
def Post_detail(request, pk):
    Post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/Post_detail.html', {'Post': Post})
def Post_new(request):
    form = PostForm()
    return render(request, 'blog/Post_edit.html', {'form': form})