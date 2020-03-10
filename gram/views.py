from django.shortcuts import render, redirect
from . forms import ImageProfileForm, ImageUploadForm, CommentForm
from .models import *
from django.contrib.auth.decorators import login_required
from vote.managers import VotableManager


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()
    return render(request, 'index.html', {"images":images})

def image_upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')
    else:
        form = ImageUploadForm()
        return render(request,'upload.html', {"form":form})

def profile_info(request):
    current_user = request.user
    profile_info = Profile.objects.filter(user=current_user).first()
    posts =  request.user.image_set.all()

    return render(request, 'profile.html',{"images":posts,"profile":profile_info,"current_user":current_user})



def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('profile')

    else:
        form = ImageProfileForm()
        return render(request,'edit.html',{"form":form})



def comments(request,id):
    comments = Comments.get_comments(id)
    number = len(comments)
    return render(request,'comments.html',{"comments":comments,"number":number})




def add_comment(request,id):
    current_user = request.user
    image = Image.get_single_photo(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image_id = id
            comment.save()
        return redirect('index')

    else:
        form = CommentForm()
        return render(request,'new_comment.html',{"form":form,"image":image})

@login_required (login_url='/accounts/register/')
def like_images(request,id):
    image =  Image.get_single_photo(id)
    user = request.user
    user_id = user.id
    if user.is_authenticated:
        uplike = image.votes.up(user_id)
        image.likes = image.votes.count()
        image.save()
    return redirect('index')

def search_user(request):
    if 'search_user' in request.GET and request.GET["search_user"]:
        search_term = request.GET.get("search_user")
        searched_user = User.objects.filter(username__icontains=search_term)
        message = f"{search_term}"
        return render(request, 'search_results.html', {"message": message, "users": searched_user})
    else:
        message = "No results found "
    return render(request, 'search_results.html',{"message":message})

