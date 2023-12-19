from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserProfileForm, CommentForm, PostForm
from .models import UserProfile, Post
from django.db import models
from django.views import generic, View
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect


@login_required
def create_post(request):
    if not request.user.is_superuser:
        return redirect('')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.status = 1
            new_post.save()
            return redirect('post_detail', slug=new_post.slug)
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()


        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'profile/edit_profile.html', {'form': form, 'user_profile': user_profile})


def home_view(request):
    return render(request, 'index.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})


@login_required
def view_profile(request):
    user = request.user
    return render(request, 'profile/view_profile.html', {'user': user})
