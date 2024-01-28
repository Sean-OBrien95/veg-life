from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegistrationForm, ProfileForm, CommentForm, PostForm
from .models import UserProfile, Post, Comment, Bookmark
from django.db import models
from django.views import generic, View
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.contrib import messages


# View to create a new post
@login_required
def create_post(request):

    # Redirect non-superusers
    if not request.user.is_superuser:
        return redirect('')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.status = 1

            # Pull featured image if one stored
            if 'featured_image' in request.FILES:
                new_post.featured_image = request.FILES['featured_image']

            new_post.save()

            messages.success(request, 'Post created successfully!')

            return redirect('post_detail', slug=new_post.slug)
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


# Class-based view for displaying a list of posts
class PostList(generic.ListView):

    model = Post
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        # Get the value of 'q' from the request's GET parameters
        query = self.request.GET.get('q')
        if query:
            # If a search query is provided, filter posts based on title,
            # author's username, or tags
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(author__username__icontains=query) |
                Q(tags__icontains=query)
            ).distinct()
        else:
            # If no search query is provided, filter published posts
            # by status and order by creation date
            return Post.objects.filter(status=1).order_by('-created_on')


# Class-based view for displaying post details and handling comments
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # Retrieve all published posts
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')

        # Check if current user has liked the post
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Check if current user has bookmarked the post
        bookmarked = False
        if request.user.is_authenticated:
            bookmarked = Bookmark.objects.filter(
                user=request.user, post=post).exists()

        # Render the post_detail.html template with relevant context data
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "bookmarked": bookmarked,
                "comment_form": CommentForm(),
                "author_id": post.author.id
            },
        )

    def post(self, request, slug, *args, **kwargs):
        # Retrieve all published posts
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        # Get the IDs of comments liked by the user
        liked_comments = list(
            request.user.comment_likes.all().values_list('id', flat=True))
        comments = post.comments.filter(approved=True).order_by('created_on')

        # Check if the current user has liked the post
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Create a CommentForm instance with POST data
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.commentor = request.user
            comment.save()
        else:
            comment_form = CommentForm()

        # Render the post_detail.html template with relevant context data
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


# Class-based view for handling post likes
class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# View to handle liking/unliking a comment
@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# View to edit user profile
@login_required
def edit_profile(request):
    try:
        # Attempt to retrieve the user's profile using the UserProfile model
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If the user profile does not exist, create a new one for the user
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        # If the form is submitted with POST data
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            # If the form is valid, save the form data to
            # update the user profile
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('view_profile')
    else:
        # If the form is not submitted (GET request),
        # initialize the form with the user's profile data
        form = ProfileForm(instance=user_profile)

    return render(request, 'profile/edit_profile.html',
                  {'form': form, 'user_profile': user_profile})


# View to handle user registration
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


# View to display user profile
@login_required
def view_profile(request, user_id=None):
    if user_id:
        user = get_object_or_404(User, pk=user_id)
    else:
        user = request.user

    return render(request, 'profile/view_profile.html', {'user': user})


# View to edit a post
@login_required
def edit_post(request, slug):

    post = get_object_or_404(Post, slug=slug)

    # Check if the current user has permission to edit the post
    if request.user != post.author:
        return HttpResponseForbidden(
            "You don't have permission to edit this post.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # If the form is valid, save the form data to update the post
            edited_post = form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', slug=edited_post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})


# View to confirm post deletion
def confirm_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user == post.author:
        return render(request, 'confirm_delete.html', {'post': post})

    return redirect('home')


# View to delete a post
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user == post.author:
        post.delete()
        messages.error(request,
                       'Post has been deleted', extra_tags='toast-red')

    return redirect('home')


# View to confirm profile deletion
@login_required
def confirm_profile_delete(request):
    return render(request, 'confirm_profile_delete.html')


# View to delete a user profile
@login_required
def delete_profile(request, user_id):

    user = get_object_or_404(User, pk=user_id)

    # Check if the logged-in user matches the user whose
    # profile is being deleted
    if request.user == user:
        try:
            profile = UserProfile.objects.get(user=user)
            profile.delete()

            # Retrieve and delete all comments made by the user
            user_comments = Comment.objects.filter(commentor=user)
            user_comments.delete()

            user.blog_likes.clear()

        except UserProfile.DoesNotExist:
            pass

        # Delete the user account
        user.delete()

        messages.error(request, 'Profile has been deleted')

        return redirect('home')
    else:
        return redirect('home')


# View to delete a comment
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == comment.commentor:
        post_slug = comment.post.slug

        comment.delete()

        return redirect('post_detail', slug=post_slug)
    else:
        return redirect('error_page')


# View to handle comment approval by a superuser
@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='home')
def comment_approval(request):

    pending_comments = Comment.objects.filter(approved=False)

    if request.method == 'POST':
        # Retrieve the comment_id and action from the submitted form
        comment_id = request.POST.get('comment_id')
        action = request.POST.get('action')

        comment = get_object_or_404(Comment, pk=comment_id)

        # Process the chosen action (approve or decline) for the comment
        if action == 'approve':
            comment.approved = True
            comment.save()

            return redirect('post_detail', slug=comment.post.slug)

        elif action == 'decline':
            # Delete the comment if the action is 'decline'
            comment.delete()

            return redirect('post_detail', slug=comment.post.slug)

    return render(request, 'comment_approval.html',
                  {'pending_comments': pending_comments})


# View to toggle bookmark for a post
@login_required
def toggle_bookmark(request, post_id):

    user = request.user
    post = get_object_or_404(Post, id=post_id)

    # Check if a bookmark already exists for the user and post
    if Bookmark.objects.filter(user=user, post=post).exists():
        Bookmark.objects.filter(user=user, post=post).delete()
    else:
        Bookmark.objects.create(user=user, post=post)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# View to display user bookmarks
@login_required
def user_bookmarks(request):
    user = request.user
    bookmarks = Bookmark.objects.filter(user=user)
    return render(request, 'user_bookmarks.html', {'bookmarks': bookmarks})
