from django.shortcuts               import render
from django.utils                   import timezone
from .models                        import Post, Entry
from django.shortcuts               import render, get_object_or_404
from .forms                         import PostForm, EntryForm
from django.shortcuts               import redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

# Blog views
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/post_list.html', {
        'posts': posts
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# CV views
def cv(request):
    return render(request, 'cv/entry_list.html')

# Entry views
def entry_list(request):
    entries = Entry.objects.order_by('start_date').reverse()
    return render(request, 'cv/cv_static.html', {
        'entries': entries
    })

def entry_details(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'cv/entry_details.html', {'entry': entry})

@login_required
def entry_new(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('entry_details', pk=entry.pk)
    else:
        form = EntryForm()
    return render(request, 'cv/entry_edit.html', {'form': form})

@login_required
def entry_edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('entry_details', pk=entry.pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'cv/entry_edit.html', {'form': form})
