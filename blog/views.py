from django.shortcuts   import render
from django.utils       import timezone
from .models            import Post, Entry, EducationEntry, PersonalProfile
from django.shortcuts   import render, get_object_or_404
from .forms             import PostForm, EntryForm, EducationEntryForm, PersonalProfileForm
from django.shortcuts   import redirect

def home(request):
    return render(request, 'home.html')

# Blog views
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {
        'posts': posts
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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
    return render(request, 'cv/cv_static.html')

# Entry views
def entry_list(request):
    entries = Entry.objects.order_by('start_date')
    return render(request, 'cv/cv_static.html', {
        'entries': entries
    })

def entry_details(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'cv/entry_details.html', {'entry': entry})

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

# Education Entry views
def educationEntry_list(request):
    educationEntries = EducationEntry.objects.order_by('end_date')
    return render(request, 'cv/cv_static.html', {
        'educationEntries': educationEntries
    })

def educationEntry_details(request, pk):
    educationEntry = get_object_or_404(EducationEntry, pk=pk)
    return render(request, 'cv/educationEntry_details.html', {
        'educationEntry': educationEntry
    })

def educationEntry_new(request):
    if request.method == "POST":
        form = EducationEntryForm(request.POST)
        if form.is_valid():
            educationEntry = form.save(commit=False)
            educationEntry.save()
            return redirect('educationEntry_details', pk=educationEntry.pk)
    else:
        form = EducationEntryForm()
    return render(request, 'cv/educationEntry_edit.html', {'form': form})

def educationEntry_edit(request, pk):
    educationEntry = get_object_or_404(EducationEntry, pk=pk)
    if request.method == "POST":
        form = EducationEntryForm(request.POST, instance=educationEntry)
        if form.is_valid():
            educationEntry = form.save(commit=False)
            educationEntry.save()
            return redirect('educationEntry_details', pk=educationEntry.pk)
    else:
        form = EducationEntryForm(instance=educationEntry)
    return render(request, 'cv/educationEntry_edit.html', {'form': form})


# def personalprofile(request):
#    return render(request, 'personalprofile.html')
#
# def personalprofile_edit(request):
#    personalprofile = get_object_or_404(PersonalProfile)
#    if request.method == "POST":
#        form = PersonalProfileForm(request.POST, instance=personalprofile)
#        if form.is_valid():
#            personalprofile = form.save(commit=False)
#            personalprofile.last_updated = timezone.now()
#            personalprofile.save()
#            return redirect('personalprofile')
#    else:
#        form = PersonalProfileForm(instance=personalprofile)
#    return render(request, 'cv/personalprofile.html', {'form': form})
