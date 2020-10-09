from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def Post_list(request):
    Posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/Post_list.html', {'Posts': Posts}) 
def Post_new(request):
    form = Postform()
    return render(request, 'blog/Post_edit.html', {'form': form})
def Post_detail(request, pk):
    Post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/Post_detail.html', {'Post': Post})
def Post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post = form.save(commit=False)
            Post.author = request.user
            Post.published_date = timezone.now()
            Post.save()
            return redirect('Post_detail', pk=Post.pk)
    else:
    	form = Postform()
    return render(request, 'blog/Post_edit.html', {'form': form})