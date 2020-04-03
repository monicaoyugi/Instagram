from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import UserCreationForm, ProfileEditForm, CommentForm


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    comments = Comment.objects.all()
    user_profile = Profile.objects.get(user=user)
    posts = Post.objects.all()
    profiles = Profile.objects.all()
    context = {
        "comments":comments,
        "posts": posts,
        "profiles": profiles,
        "user_profile":user_profile
    }
    return render(request, 'index.html', context)

@login_required
def add_comment(request):
    current_user = request.user

    if request.method == 'POST':
        c_form = CommentForm(request.POST, instance=request.user)
    else:
        c_form = CommentForm(instance=request.user)

    if c_form.is_valid():
        print(c_form)
        c_form.save()

        messages.success(
            request, f'comment created successfully')
        return redirect('index')
    context = {
        'c_form': c_form
    }
    return render(request, 'new_comment.html', context)
@login_required
def profile_info(request):
    profiles = Profile.objects.filter(user=request.user)
    if not profiles.first():
        profile = Profile.objects.create(user=request.user)
        profile.save()
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(author=request.user)
    context = {
        "profile": profile,
        "posts":posts
    }
    return render(request, 'profile.html', context)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['author', 'post', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def profile_edit(request):
    current_user = request.user

    if request.method == 'POST':
        p_form = ProfileEditForm(
            request.POST, request.FILES,instance=request.user.profile
        )
    else:
        p_form = ProfileEditForm(instance=request.user.profile)

    if  p_form.is_valid():
        p_form.save()

        messages.success(
            request, f'Your profile has been updated successfully')
        return redirect('profile_edit')
    context = {
        'p_form': p_form
    }
    return render(request, 'edit_profile.html', context)

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        name = request.GET.get("article")
        users= Profile.get_user(name)
        message = f"{name}"

        return render(request, 'search_results.html',{"message":message,"users": users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_results.html', {"message": message})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            messages.success(f'account for {username} created successfully')
            print(form.cleaned_data)
            profile = Profile.objects.create(user=form.cleaned_data)
            profile.save()
            return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'registration/registration.html', {form:form})